#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
from json import dumps
from requests import get

if __name__ == "__main__":
    data = {}
    for user_id in get('https://jsonplaceholder.typicode.com/users/').json():
        users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(user_id)).json()
        todo_list = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(user_id)).json()
        data[str(user_id)] = [dict(task=element['title'], completed=element['completed'],
                                    username=users['username']) for element in todo_list]
        
        with open('todo_all_employees.json', mode='w') as file:
            file.write(dumps(data))
