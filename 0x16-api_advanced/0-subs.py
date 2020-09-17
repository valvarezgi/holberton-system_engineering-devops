#!/usr/bin/python3
"""Makes connection with api"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a given subreddit"""
    user = {'user-agent': 'valvarezgi'}
    req = get('https://www.reddit.com/r/{}/about.json'.
              format(subreddit), headers=user)
    subs = req.json()
    if req.status_code == 404:
        return 0
    else:
        return(subs['data']['subscribers'])
