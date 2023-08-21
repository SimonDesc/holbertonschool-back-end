#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script_name employee_id")
        sys.exit(1)

    employee_id = {"id": sys.argv[1]}

    # Get the name of the employee
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/", params=employee_id
    )
    if response.status_code != 200:
        print("Error fetching employee data")
        sys.exit(1)

    employee_data = response.json()
    name_employee = employee_data[0]["name"]

    # Get the total number of tasks
    user_id = {"userId": sys.argv[1]}
    task_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos", params=user_id
    )
    if task_response.status_code != 200:
        print("Error fetching task data")
        sys.exit(1)

    tasks_data = task_response.json()
    number_total_task = len(tasks_data)

    # Get the number of tasks completed
    tasks_completed = 0
    tasks_title = []

    for task in tasks_data:
        if task["completed"]:
            tasks_completed += 1
            tasks_title.append(task["title"])

    # print final result
    print(
        f"Employee {name_employee} is done with tasks"
        f"({tasks_completed}/{number_total_task}):"
    )

    for title in tasks_title:
        print("\t" + title)
