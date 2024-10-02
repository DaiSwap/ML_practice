from flask import Flask, request, jsonify

app = Flask(__name__)
"""
@app.route("/")
def home():
    return "Home"
    """
#Creating first root inside of flask

#GET request data from a specified source 
#POST Create a resource
#PUT update a resource
#DELETE delete a resource

#cretating get route - path parameter (a dynamic value passing in url)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name":"DaiSwap",
        "email": "daiswap@exampe.com"
    }
#query parameter     
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200 #flask parsing this value and returning as jsonify value & 200 is default status code for success
    

if __name__ == "__main__":
    app.run(debug=True)