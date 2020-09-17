#!/usr/bin/python3
"""Makes connection with api"""
from requests import get


def recurse(subreddit, host_list=[], after=None):
    """Returns a list containing the titles of all hot
    articles for a given subreddit"""
    user = {'user-agent': 'valvarezgi'}
    url = 'https://www.reddit.com/'
    query = '/r/{}/hot.json?after={}'.format(subreddit, after)
    req = get(url + query, headers=user)
    top_posts = req.json().get('data', {}).get('children', [])
    after = req.json().get('data', {}).get('after', None)
    if not top_posts:
        return None
    for post in top_posts:
        host_list.append(post.get('data').get('title'))
    if not after:
        return host_list
    return recurse(subreddit, host_list, after)
