#!/usr/bin/python3
""" 433 34  """

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store user data
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    return jsonify(list(users.keys()) if users else [])

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()

        if not user_data:
            return jsonify({"error": "Invalid JSON"}), 400

        username = user_data.get("username")
        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        users[username] = {
            "username": username,
            "name": user_data.get("name"),
            "age": user_data.get("age"),
            "city": user_data.get("city")
        }

        return jsonify({"message": "User added", "user": users[username]}), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True)
