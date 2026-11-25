"""Day 10: Extracting web data with BeautifulSoup."""

import sys
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError as error:
    if error.name not in {"requests", "bs4"}:
        raise
    print(
        "Required packages are missing. Install them using: "
        "pip install requests beautifulsoup4",
        file=sys.stderr,
    )
    raise SystemExit(1)


# Question 1: Parse the sample menu and print every link destination.
html_menu = """
<ul class="nav-links">
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About Us</a></li>
    <li><a href="/contact">Contact</a></li>
</ul>
"""

menu_soup = BeautifulSoup(html_menu, "html.parser")
menu_links = menu_soup.find_all("a")

print("Question 1: Menu link destinations")
for link in menu_links:
    print(link.get("href", "No destination found"))

# Question 2: Fetch example.com, then extract the page title and a link.
print("\nQuestion 2: Data from example.com")
try:
    response = requests.get("https://example.com", timeout=10)
    response.raise_for_status()
    page_soup = BeautifulSoup(response.text, "html.parser")

    title = page_soup.find("title")
    if title is None:
        print("Page title: Not found")
    else:
        print(f"Page title: {title.get_text(strip=True)}")

    page_link = page_soup.find("a", href=True)
    if page_link is None:
        print("Link destination: Not found")
    else:
        destination = urljoin(response.url, page_link["href"])
        print(f"Link destination: {destination}")
except requests.HTTPError as error:
    print(f"HTTP error while fetching example.com: {error}")
except requests.RequestException as error:
    print(f"Request failed while fetching example.com: {error}")
