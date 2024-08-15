#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    - If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/yosefbenti)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            
            if not children:
                print(None)
            else:
                for child in children:
                    title = child.get("data", {}).get("title", "None")
                    print(title)
        else:
            print(None)
    
    except requests.RequestException:
        print(None)
