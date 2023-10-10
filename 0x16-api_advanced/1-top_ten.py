#!/usr/bin/python3
"""
Script prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that prints the hot posts of a subreddit.
    """
    response = requests.get(f"https://www.reddit.com/r/{subreddit}" +
                            "/hot.json?limit=10",
                            headers={"User-Agent": "custom_user_agent"})
    if response.status_code == 200:
        for post in response.json().get("data", {}).get("children", []):
            print(post["data"]["title"])
    else:
        print(None)
