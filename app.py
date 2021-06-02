from flask import Flask,request,jsonify
from flask_cors import CORS
import movie_recommendations

app = Flask(__name__)
CORS(app) 
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
        res = movie_recommendations.results(request.args.get('title'))
        return jsonify(res)
		
@app.route('/genre', methods=['GET'])
def recommend_movies_based_on_genres():
        res = movie_recommendations.results_on_genres(request.args.get('genre_type'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)
