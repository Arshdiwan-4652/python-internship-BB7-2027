"""Day 11: Introduction to Flask and routing."""

import sys

try:
    from flask import Flask
except ModuleNotFoundError as error:
    if error.name != "flask":
        raise
    print("Flask is not installed. Install it using: pip install flask", file=sys.stderr)
    raise SystemExit(1)


# Question 1:
# A web server receives requests from browsers and sends back web pages or data.
# The @app.route("/") decorator tells Flask to call the connected function when
# a visitor opens the site's home-page URL.

# Question 2: Create the Flask application.
app = Flask(__name__)


# The home page route.
@app.route("/")
def home():
    return "Welcome to the homepage!"


# The contact page route.
@app.route("/contact")
def contact():
    return "Contact us at support@example.com"


# The help page route.
@app.route("/help")
def help_page():
    return "This is the help page. How can we support you?"


# Start the server only when this file is run directly.
if __name__ == "__main__":
    print("Open these Task 1 URLs in your browser:")
    print("Home:    http://127.0.0.1:5000/")
    print("Contact: http://127.0.0.1:5000/contact")
    print("Help:    http://127.0.0.1:5000/help")
    app.run(debug=True, port=5000, use_reloader=False)
