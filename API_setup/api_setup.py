from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"
#Creating first root inside of flask
if __name__ == "__main__":
    app.run(debug=True)