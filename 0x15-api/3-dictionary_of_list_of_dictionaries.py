#!/usr/bin/python3
"""
Script that uses a REST API to return information about employees.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    employees = requests.get(users_url).json()
    tasks = requests.get(todos_url).json()
    employee_tasks = {}

    for employee in employees:
        emp_id = employee["id"]
        emp_name = employee["username"]
        employee_tasks[emp_id] = []

        for task in tasks:
            if task["userId"] == emp_id:
                employee_tasks[emp_id].append({
                    "username": emp_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

    json_file = "todo_all_employees.json"
    with open(json_file, mode="w") as file:
        json.dump(employee_tasks, file)
