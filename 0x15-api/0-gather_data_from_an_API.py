#!/usr/bin/python3
"""Returns TODO list progress for a given employee"""
from requests import get
from sys import argv

if __name__ == "__main__":

    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    todo_list = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(argv[1])).json()
    output = []

    for todo in todo_list:
        if todo.get('completed') is True:
            output.append(todo.get('title'))
    print('Employee {} is done with tasks({}/{}):'
          .format(users.get('name'), len(output), len(todo_list)))
    for element in output:
        print('\t ' + element)
