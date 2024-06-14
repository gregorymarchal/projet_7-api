from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"Hello": "World"})
