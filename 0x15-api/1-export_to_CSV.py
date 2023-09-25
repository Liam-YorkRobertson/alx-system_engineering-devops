#!/usr/bin/python3
"""
Script that uses a REST API to return information about employees.
"""
import csv
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

    csv_file = f"{emp_id}.csv"
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])

        for task in tasks:
            task_completed = task.get("completed")
            task_title = task.get("title")
            writer.writerow([emp_id, emp_name, task_completed, task_title])
