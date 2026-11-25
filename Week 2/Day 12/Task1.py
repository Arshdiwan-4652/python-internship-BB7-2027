"""Day 12: Serving HTML templates with Flask and Jinja2.

HTML templates keep page structure and styling separate from Python logic,
which makes web pages easier to read and update than raw HTML strings.

In Jinja2, {{ variable }} displays a value in the page. A {% statement %}
such as if or for controls page logic without directly displaying itself.
"""

import sys

try:
    from flask import Flask, render_template
except ModuleNotFoundError as error:
    if error.name != "flask":
        raise
    print("Flask is not installed. Install it using: pip install flask", file=sys.stderr)
    raise SystemExit(1)


# Create the Flask application. Flask will look for HTML files in templates/.
app = Flask(__name__)


# Send profile information to the Jinja2 template for display.
@app.route("/profile")
def profile():
    return render_template(
        "profile.html",
        name="Arsh",
        age=22,
        languages=["Python", "Java", "JavaScript"],
    )


# Run the local development server when this file is started directly.
if __name__ == "__main__":
    print("Open the profile dashboard at http://127.0.0.1:5000/profile")
    app.run(debug=True, port=5000, use_reloader=False)
