"""Day 11: Dynamic URL variables and JSON responses."""

import sys

try:
    from flask import Flask, jsonify
except ModuleNotFoundError as error:
    if error.name != "flask":
        raise
    print("Flask is not installed. Install it using: pip install flask", file=sys.stderr)
    raise SystemExit(1)


app = Flask(__name__)


# Question 1: Flask converts the URL part to an integer for this route.
@app.route("/square/<int:number>")
def square(number):
    return f"The square of {number} is {number * number}"


# Question 2: jsonify creates a proper JSON response from this dictionary.
@app.route("/api/status")
def status():
    return jsonify(
        {
            "status": "active",
            "uptime": "24h",
            "version": 1.0,
        }
    )


# Question 3: Add the two integer values from the URL.
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


# Start the server on a different port from Task1.py.
if __name__ == "__main__":
    print("Open these Task 2 URLs in your browser:")
    print("Square: http://127.0.0.1:5001/square/5")
    print("Status: http://127.0.0.1:5001/api/status")
    print("Add:    http://127.0.0.1:5001/add/10/20")
    app.run(debug=True, port=5001, use_reloader=False)
