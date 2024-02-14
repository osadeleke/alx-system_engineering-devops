#!/usr/bin/python3
"""
get the top ten hot topics of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    get the top ten hot topics of a subreddit
    """
    results = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={"User-Agent": "my bot 0.1"})
    if results.status_code == 200:
        response_data = results.json()
        titles = response_data['data']['children']
        for title in titles:
            print(title['data']['title'])
    else:
        print(None)
