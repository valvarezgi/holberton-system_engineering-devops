#!/usr/bin/python3
"""exports data in JSON format"""
from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    todo_list = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(argv[1])).json()
    with open('{}.json'.format(argv[1]), mode='w') as file_json:
        data = {}
        user_id = users.get('id')
        data[user_id] = []

        for todo in todo_list:
            data[user_id].append({
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': users.get('username')})
        dump(data, file_json)
