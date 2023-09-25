#!/usr/bin/python3
"""
Script that uses a REST API to return information about employees.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = int(argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    user = requests.get(user_url).json()
    emp_name = user.get("username")
    tasks = requests.get(tasks_url).json()
    user_data = {emp_id: []}

    for task in tasks:
        task_title = task.get("title")
        task_completed = task.get("completed")
        user_data[emp_id].append({
            "task": task_title,
            "completed": task_completed,
            "username": emp_name
        })

    json_file = f"{emp_id}.json"
    with open(json_file, mode="w") as file:
        json.dump(user_data, file)
