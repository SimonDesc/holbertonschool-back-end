#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import requests
import sys
import csv

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


def main():
    if len(sys.argv) < 2:
        print("Usage: script_name employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Retrieve employee related data
    employee_data = get_employee_data(employee_id)
    name_employee = employee_data.get("username")

    # Retrieve tasks related data
    tasks_data = get_tasks_data(employee_id)

    new_list = []
    for task in tasks_data:
        inner_list = []
        inner_list = [
            str(task["userId"]),
            str(name_employee),
            str(task["completed"]),
            str(task["title"]),
        ]
        new_list.append(inner_list)

    with open("USER_ID.csv", "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(new_list)


if __name__ == "__main__":
    main()
