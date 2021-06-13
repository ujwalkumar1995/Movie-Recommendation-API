# Movie-Recommendation-API
Movie Recommendation API build using python, flask and deployed on the heorku platform.

* Movie recommendation API that has been built using Python and deployed on Heroku. This API is based on the Content-Based Filtering technique used in recommendation systems where we recommend items to a user based on the input item's attributes. 
* We have used the IMDB movies dataset available on Kaggle to fetch the recommendations. 
* We first perform preprocessing on the dataset, remove null values and remove columns which would not ideally have great impact on the recommendations like release date, homepage, budget etc. The preprocessing part has been done in jupyter notebooks using pandas library from python.
* We have used different machine learning techniques to make these recommendations  like one hot encoding, TF-IDF Vectorizer, Cosine similarity etc.
* The API is built using flask framework and is hosted on the Heroku Platform. 

## API Features: 

The API has two capabilities:

### Genre Based Recommendation

The API is capable for recommending top rated movies of a particular Genre. It filters out the movies of particular genre by using one hot encoding technique and then it fetches the top movies based on the ratings of the users.

### Movie Based Recommendation 

The API is capable for recommending similar movies to a particular movie. This is done with the help of using machine learning techniques / algorithms like TF-IDF Vectorizer, Cosine similarity, Sparse Matrix etc.

## Project Structure Description

### Processed_Dataset

* Contains the dataset that we have used for our recommendations after preprocessing has been done on them.

### Python Notebooks

* Contains the python notebooks that we used for preprocessing.

### Procfile

* Contains information about how to run the application.

### __pycache__ folder

* When we run a program in python, the interpreter compiles it to bytecode first and stores it in the __pycache__ folder. This is done behind automatically by the python environment.

### app.py

* Contains the routing functions that route the endpoint of the API.

### movie_recommedations.py

* This file contains the functions which use various machine learning techniques to filter out the result based on the end point.

### requirements.txt

* This has all the dependencies required to deploy our application on Heroku.

### runtime.txt

* Specifies the python version to be used.

