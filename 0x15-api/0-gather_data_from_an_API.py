#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])

        user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
        employee_name = user_data.get("name")

        tasks_data = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()
        completed_tasks = [t["title"] for t in tasks_data if t.get("completed")]
        total_tasks = len(tasks_data)

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task}")
