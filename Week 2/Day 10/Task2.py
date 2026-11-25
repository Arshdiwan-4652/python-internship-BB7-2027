"""Day 10: Scraping etiquette and HTTP headers."""

import sys
import time

try:
    import requests
except ModuleNotFoundError as error:
    if error.name != "requests":
        raise
    print(
        "Required packages are missing. Install them using: "
        "pip install requests beautifulsoup4",
        file=sys.stderr,
    )
    raise SystemExit(1)


# Question 1:
# robots.txt tells automated visitors which parts of a website its owner
# allows or disallows them to crawl. Check it before scraping a site.
#
# When scraping several pages, time.sleep() pauses between requests. This
# reduces the load on the website and helps avoid sending requests too quickly.
print("Question 1: Scraping etiquette")
print("Check a site's robots.txt to learn which pages it allows crawlers to visit.")
print("Use time.sleep() between requests to avoid sending them too quickly.")

# Question 2: Request each post and wait two seconds between requests.
post_urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

print("\nQuestion 2: Request post URLs")
for index, url in enumerate(post_urls):
    try:
        response = requests.get(url, timeout=10)
        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
    except requests.RequestException as error:
        print(f"URL: {url}")
        print(f"Request failed: {error}")

    # Pause only when another request will follow.
    if index < len(post_urls) - 1:
        time.sleep(2)

# Question 3: Send a custom User-Agent and check what the server received.
print("\nQuestion 3: Custom User-Agent")
headers = {"User-Agent": "MyStudyBot/1.0"}

try:
    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()
    header_data = response.json()
    received_user_agent = header_data.get("headers", {}).get("User-Agent", "Not found")

    print(f"User-Agent received by server: {received_user_agent}")
    print(f"Matches MyStudyBot/1.0: {received_user_agent == 'MyStudyBot/1.0'}")
except requests.HTTPError as error:
    print(f"HTTP error while checking the User-Agent: {error}")
except requests.RequestException as error:
    print(f"Request failed while checking the User-Agent: {error}")
except ValueError as error:
    print(f"Could not read the server's JSON response: {error}")
