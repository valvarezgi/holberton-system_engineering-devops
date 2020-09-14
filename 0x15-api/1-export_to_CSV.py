#!/usr/bin/python3
"""exports data in CSV format"""
from csv import QUOTE_ALL, writer
from requests import get
from sys import argv

if __name__ == "__main__":
    users = get('https://jsonplaceholder.typicode.com/users/{}'
                .format(argv[1])).json()
    todo_list = get('https://jsonplaceholder.typicode.com/todos?userId={}'
                    .format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), mode='w') as file_csv:
        writer_csv = writer(file_csv, delimiter=',', quoting=QUOTE_ALL)
        for element in todo_list:
            writer_csv.writerow([users['id'], users['username'],
                                element['completed'], element['title']])
