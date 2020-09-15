#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
from requests import get

if __name__ == "__main__":

    user_id = {}
    filename = "todo_all_employees.json"
    req = get('https://jsonplaceholder.typicode.com/todos')
    req_id = get('https://jsonplaceholder.typicode.com/users/')
    with open("todo_all_employees.json", mode="w") as f:
        d = {j.get("id"): [{'task': i.get('title'),
             'completed': i.get('completed'),
                            'username': j.get('username')} for i in req.json()
                           if j.get("id") == i.get('userId')]
             for j in req_id.json()}
        json.dump(d, f)
