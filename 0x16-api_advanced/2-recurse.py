#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list of titles of all hot posts on a given subreddit."""

import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        count += data.get("dist", 0)
        for child in data.get("children", []):
            hot_list.append(child.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
    else:
        return None
