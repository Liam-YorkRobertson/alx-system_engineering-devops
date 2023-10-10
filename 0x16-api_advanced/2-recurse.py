#!/usr/bin/python3
"""
Recursive function that returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that returns the hot articlesfor a given subreddit
    """
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            params={"limit": 100, "after": after},
                            headers={"User-Agent": "custom_user_agent"})

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        hot_list.extend(post["data"]["title"] for post in posts)
        after = data.get("after")

        return (recurse(subreddit, hot_list, after) if after else hot_list)

    return (None)
