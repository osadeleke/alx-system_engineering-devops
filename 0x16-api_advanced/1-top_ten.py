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
    response_data = results.json()
    # if results.status_code != 200:
    #     print(None)
    # else:
    #     for i in range(10):
    #         print(response_data['data']['children'][i]['data']['title'])
    titles = response_data['data']['children']
    print(titles)

    # print(response_data)