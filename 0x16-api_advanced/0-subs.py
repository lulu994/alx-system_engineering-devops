#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Your_Custom_User_Agent_1.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
