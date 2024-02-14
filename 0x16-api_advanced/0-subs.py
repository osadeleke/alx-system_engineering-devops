#!/usr/bin/python3
"""
module for number of subscribers for subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers for subreddit
    """
    results = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={'User-agent': 'my bot 0.1'})

    if results.status_code == 200:
        response_data = results.json()
        subscribers = response_data['data']['subscribers']
        return subscribers
    else:
        return 0
