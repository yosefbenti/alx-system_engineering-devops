#!/usr/bin/python3
""" Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data', {}).get('children', [])
            for i in range(min(10, len(children))):
                print(children[i].get('data', {}).get('title', "None"))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")
