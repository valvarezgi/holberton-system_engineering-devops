#!/usr/bin/python3
"""Makes connection with api"""
from requests import get


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a
    given subreddit"""
    user = {'user-agent': 'valvarezgi'}
    req = get('https://www.reddit.com/r/{}/hot.json?limit=10'
              .format(subreddit), headers=user)
    subs = req.json()
    if req.status_code == 404:
        print (None)
    else:
        for child in range(len(subs['data']['children'])):
            print(subs['data']['children'][child]['data']['title'])
