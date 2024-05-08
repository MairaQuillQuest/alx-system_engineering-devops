#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import urllib.parse

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(urllib.parse.quote(subreddit.lower()))
    headers = {
        "User-Agent": "MyBot/0.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    if response.is_redirect:
        return 0  # Handle redirects
    results = response.json().get("data")
    return results.get("subscribers")
