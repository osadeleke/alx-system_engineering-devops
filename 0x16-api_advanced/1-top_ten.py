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
    final_results = results.json().get('data').get('children')

    for result in final_results:
        print(result)