import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


clf = None
with open("model.pkl", "rb") as file:
    clf = pickle.load(file)
    print("Load worked")


@app.route("/")
def index():
    return "Server On."


@app.route('/call_predict', methods=['POST'])
def call_predict():
    content = request.get_json()
    data = content['data']
