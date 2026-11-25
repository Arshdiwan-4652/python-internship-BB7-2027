"""Day 8: How the web works and the requests library."""

import sys

try:
    import requests
except ModuleNotFoundError as error:
    if error.name != "requests":
        raise
    print("Requests is not installed. Install it using: pip install requests", file=sys.stderr)
    raise SystemExit(1)


# Question 1: Explain the basic client-server relationship and HTTP GET.
print("Question 1: How the web works")
print("A client is an app or device that asks for information, such as a browser.")
print("A server receives the request and sends back a response.")
print("An HTTP GET request asks a server to return information from a URL.")

# Question 2: Request a page that intentionally returns HTTP 404.
print("\nQuestion 2: Request a page with a 404 status")
try:
    response = requests.get("https://httpbin.org/status/404", timeout=10)
    print(f"HTTP status code: {response.status_code}")
    response.raise_for_status()
    print("The request succeeded.")
except requests.HTTPError as error:
    print(f"HTTP error: {error}")
except requests.RequestException as error:
    print(f"Request failed: {error}")

# Question 3: Ask for a URL and report whether it returned exactly HTTP 200.
print("\nQuestion 3: Check a website")
website_url = input("Enter a website URL (for example, https://example.com): ").strip()
try:
    website_response = requests.get(website_url, timeout=10)
except (requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema,
        requests.exceptions.MissingSchema) as error:
    print(f"Invalid URL: {error}")
    print("Website is Offline")
except requests.ConnectionError as error:
    print(f"Connection error: {error}")
    print("Website is Offline")
except requests.Timeout as error:
    print(f"Request timed out: {error}")
    print("Website is Offline")
except requests.RequestException as error:
    print(f"Request error: {error}")
    print("Website is Offline")
else:
    if website_response.status_code == 200:
        print("Website is Online")
    else:
        print(f"Received HTTP status code: {website_response.status_code}")
        print("Website is Offline")
