#Necessary Library Imports
import pandas as pd
import scipy.sparse as sp
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Convert Movie Titles to LowerCase
def covert_to_lowercase():
        movie_data = pd.read_csv('Processed_Dataset/Recommendations_DataSet_Movie.csv')
        movie_data['original_title'] = movie_data['original_title'].str.lower()
        return movie_data

#Combine genres and cast into a single string
def combine_data(data):
        data_recommend = data.drop(columns=['movie_id', 'original_title','plot'])
        data_recommend['combine'] = data_recommend[data_recommend.columns[0:2]].apply(
                                                                        lambda x: ','.join(x.dropna().astype(str)),axis=1)
        
        data_recommend = data_recommend.drop(columns=[ 'cast','genres'])
        return data_recommend

#Apply necessary machine learning techniques to make predictions        
def transform_data(data_combine, data_plot):
        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(data_combine['combine'])

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(data_plot['plot'].values.astype('U'))

        combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')
        cosine_sim = cosine_similarity(combine_sparse, combine_sparse)
        
        return cosine_sim


#Recommend top 10 movies similar to a particular movie
def recommend_movies(title, data, combine, transform):
        indices = pd.Series(data.index, index = data['original_title'])
        index = indices[title]

        sim_scores = list(enumerate(transform[index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]

        movie_indices = [i[0] for i in sim_scores]

        movie_id = data['movie_id'].iloc[movie_indices]
        movie_title = data['original_title'].iloc[movie_indices]

        recommendation_data = pd.DataFrame(columns=['Movie_Id','Name'])

        recommendation_data['Movie_Id'] = movie_id
        recommendation_data['Name'] = movie_title

        return recommendation_data
        
        
#Function that takes in genre_name as parameter and returns top 4 movies of that genre       
def get_movies_based_on_genre(genre_name):

        genre_data = pd.read_csv('Processed_Dataset/Recommendations_DataSet_Genre.csv')
        mean_vote_count = genre_data["vote_count"].mean()
        
        cols = ["movie_id", "original_title","vote_count","vote_average"]
        vote_count_condition = genre_data["vote_count"] > mean_vote_count
        genre_condition = genre_data[genre_name] == 1
        
        filtered_data = (genre_data[cols] [vote_count_condition & genre_condition])
        sorted_data = filtered_data.sort_values(by=['vote_average'],ascending=False).head(4)
        
        final_recommendation_data = pd.DataFrame(columns=['Movie_Id','Name'])
        
        final_recommendation_data['Movie_Id'] = sorted_data['movie_id']
        final_recommendation_data['Name'] = sorted_data['original_title']
        
        return final_recommendation_data
        

#Caller function that is called when we hit the /movie endpoint
def results(movie_name):
        movie_name = movie_name.lower()

        find_movie = covert_to_lowercase()
        combine_result = combine_data(find_movie)
        transform_result = transform_data(combine_result,find_movie)

        if movie_name not in find_movie['original_title'].unique():
                return 'Movie not in Database'

        else:
                recommendations = recommend_movies(movie_name, find_movie, combine_result, transform_result)
                return recommendations.to_dict('records')
                

             
#Caller function that is called when we hit the /genre endpoint 
def results_on_genres(genre_name):
        
        recommendations_on_genre = get_movies_based_on_genre(genre_name)

        if len(recommendations_on_genre) == 0:
                return 'Movie not in Database'

        else:
                return recommendations_on_genre.to_dict('records')
