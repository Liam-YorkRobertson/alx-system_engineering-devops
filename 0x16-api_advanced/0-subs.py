#!/usr/bin/python3
"""
Returns a number of subscribers a certain subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that returns the number of subs for a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "custom_user_agent"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    subs = data.get("data", {}).get("subscribers", 0)
    return (subs)
