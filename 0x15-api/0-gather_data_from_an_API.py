#!/usr/bin/python3
"""
Script that uses a REST API to return information about employees.
"""
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = int(argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    user = requests.get(user_url).json()
    emp_name = user.get("name")
    tasks = requests.get(tasks_url).json()
    completed_tasks = []
    for t in tasks:
        if t.get("completed"):
            completed_tasks.append(t["title"])

    print(f"Employee {emp_name} is done with "
          f"tasks({len(completed_tasks)}/{len(tasks)}):")

    for task in completed_tasks:
        print(f"\t {task}")
