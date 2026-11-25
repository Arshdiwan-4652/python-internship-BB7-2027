"""Day 8: Fetch and use data from JSON APIs."""

import sys

try:
    import requests
except ModuleNotFoundError as error:
    if error.name != "requests":
        raise
    print("Requests is not installed. Install it using: pip install requests", file=sys.stderr)
    raise SystemExit(1)


# Check status codes before converting any API response to JSON.
def get_json(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


# Question 3: Fetch one post and return its response as a Python dictionary.
def get_post_details(post_id):
    post = get_json(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if not isinstance(post, dict):
        raise ValueError("The post API did not return a JSON object.")
    return post


def main():
    # Question 1: Fetch todos and display the first five.
    print("Question 1: First five todos")
    try:
        todos = get_json("https://jsonplaceholder.typicode.com/todos")
        if not isinstance(todos, list):
            raise ValueError("The todos API did not return a JSON list.")
        for todo in todos[:5]:
            print(f"ID: {todo['id']}")
            print(f"Title: {todo['title']}")
            print(f"Completed: {todo['completed']}")
            print()
    except (requests.RequestException, ValueError, KeyError) as error:
        print(f"Could not load todos: {error}")

    # Question 2: Read the company name from the nested company dictionary.
    print("Question 2: User details")
    try:
        user = get_json("https://jsonplaceholder.typicode.com/users/5")
        if not isinstance(user, dict):
            raise ValueError("The user API did not return a JSON object.")
        company = user.get("company", {})
        print(f"User's Name: {user.get('name', 'Not provided')}")
        print(f"Company Name: {company.get('name', 'Not provided')}")
    except (requests.RequestException, ValueError) as error:
        print(f"Could not load user details: {error}")

    # Question 3: Call the function with post ID 12 and display its dictionary.
    print("\nQuestion 3: Post details for post 12")
    try:
        post_details = get_post_details(12)
        print(post_details)
    except (requests.RequestException, ValueError) as error:
        print(f"Could not load post details: {error}")


if __name__ == "__main__":
    main()
