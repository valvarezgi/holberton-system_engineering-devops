#!/usr/bin/python3
"""exports data in JSON format"""
from json import dumps
from requests import get
from sys import argv

if __name__ == "__main__":
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    todo_list = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(argv[1])).json()
    with open('{}.json'.format(argv[1]), mode='w') as file_json:
        todos = [dict(todos=element['title'], completed=element['completed'],
                      username=users['username']) for element in todo_list]
        data = {}
        data['{}'.format(argv[1])] = todos
        file_json.write(dumps(data))
