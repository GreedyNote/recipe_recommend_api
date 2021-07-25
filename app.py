from flask import Flask,request,jsonify
from flask_cors import CORS
import recommendation

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/movie', methods=['GET'])
def recommend_movies():
        res = recommendation.recommend(request.args.get('ingredients'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)
