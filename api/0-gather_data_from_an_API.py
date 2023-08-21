#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = BASE_URL + "/users/"
TODOS_URL = BASE_URL + "/todos"


def get_employee_data(employee_id):
    """Retrieve employee data."""
    response = requests.get(USERS_URL, params={"id": employee_id})
    if response.status_code != 200:
        print(
            f"Error fetching employee data: \
            {response.status_code} {response.text}"
        )
        sys.exit(1)
    return response.json()[0]


def get_tasks_data(user_id):
    """Retrieve tasks data."""
    response = requests.get(TODOS_URL, params={"userId": user_id})
    if response.status_code != 200:
        print(
            f"Error fetching task data: \
            {response.status_code} {response.text}"
        )
        sys.exit(1)
    return response.json()


def get_task_details(tasks_data):
    """Retrieve task details - completed count and titles."""
    tasks_completed = 0
    tasks_title = []

    for task in tasks_data:
        if task["completed"]:
            tasks_completed += 1
            tasks_title.append(task["title"])

    return tasks_completed, tasks_title


def display_result(name_employee,
                   tasks_completed,
                   number_total_task,
                   tasks_title):
    """Display the result on the standard output"""
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name_employee, tasks_completed, number_total_task
        )
    )
    for title in tasks_title:
        print("\t {}".format(title))


def main():
    if len(sys.argv) < 2:
        print("Usage: script_name employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Retrieve employee related data
    employee_data = get_employee_data(employee_id)
    name_employee = employee_data.get("name")

    # Retrieve tasks related data
    tasks_data = get_tasks_data(employee_id)
    tasks_completed, tasks_title = get_task_details(tasks_data)
    number_total_task = len(tasks_data)

    display_result(name_employee,
                   tasks_completed,
                   number_total_task,
                   tasks_title)


if __name__ == "__main__":
    main()
