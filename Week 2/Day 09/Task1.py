"""Day 09: Introduction to web scraping with BeautifulSoup."""

import sys

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError as error:
    if error.name != "bs4":
        raise
    print(
        "BeautifulSoup is not installed. Install it using: pip install beautifulsoup4",
        file=sys.stderr,
    )
    raise SystemExit(1)


# Question 1: Parse one profile card and find its name and role.
html_content = """
<div class="profile-card">
    <h2 id="name">Aman Gupta</h2>
    <p class="role">Software Engineer</p>
    <p class="location">Pune, India</p>
</div>
"""

# Tell BeautifulSoup to parse the HTML with Python's built-in html.parser.
profile_soup = BeautifulSoup(html_content, "html.parser")

# Find the name by its ID and the role by its class.
name = profile_soup.find(id="name")
role = profile_soup.find(class_="role")

print("Question 1: Profile information")
print(f"Name: {name.get_text(strip=True) if name else 'Not found'}")
print(f"Role: {role.get_text(strip=True) if role else 'Not found'}")

# Question 2: Parse a syllabus and find every element with class "topic".
html_page = """
<html>
    <head><title>Course Syllabus</title></head>
    <body>
        <h3 class="section-title">Week 1 Topics</h3>
        <p class="topic">Basic Syntax</p>
        <p class="topic">Data Structures</p>
        <h3 class="section-title">Week 2 Topics</h3>
        <p class="topic">File I/O</p>
        <p class="topic">Web scraping</p>
    </body>
</html>
"""

syllabus_soup = BeautifulSoup(html_page, "html.parser")
topics = syllabus_soup.find_all(class_="topic")

print("\nQuestion 2: Syllabus topics")
for topic in topics:
    print(topic.get_text(strip=True))
