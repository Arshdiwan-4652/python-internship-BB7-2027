"""Day 12: Flask HTML templates and Jinja2.

HTML templates let us keep a page's structure and styling in an HTML file
instead of mixing them into Python code. This makes both files easier to read
and update, while Python can focus on preparing the page's data.

In Jinja2, {{ variable }} displays a value, such as a name, on the page.
{% statement %} tells Jinja to do something, such as choose with if or repeat
with for; the statement itself is not displayed as page text.
"""

from flask import Flask, render_template

# Flask looks for HTML templates in this folder's templates/ directory.
app = Flask(__name__)


# Serve the dashboard at the home page and at the requested profile URL.
@app.route("/")
@app.route("/profile")
def profile():
    # Keep the sample profile data in Python and pass it to the HTML template.
    name = "Arsh"
    age = 22
    languages = ["Python", "Java", "JavaScript"]

    return render_template(
        "profile.html",
        name=name,
        age=age,
        languages=languages,
    )


# Start the local Flask development server when this file is run directly.
if __name__ == "__main__":
    print("Open the profile dashboard at http://127.0.0.1:5000/profile")
    app.run(debug=True, port=5000, use_reloader=False)
