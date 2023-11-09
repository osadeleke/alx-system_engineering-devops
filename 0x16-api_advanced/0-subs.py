#!/usr/bin/python3
"""
function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    # Define the URL of the Reddit API endpoint for subreddit about
    about_url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    # Send a GET request to the endpoint
    response = requests.get(about_url, headers={'User-Agent': 'YourApp/1.0'})

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()
        return int(data['data']['subscribers'])
    else:
        return 0
