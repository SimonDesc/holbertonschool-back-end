#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import json
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = BASE_URL + "/users/"
TODOS_URL = BASE_URL + "/todos"


def get_employee_data():
    """Retrieve employee data."""
    response = requests.get(USERS_URL)
    if response.status_code != 200:
        print(
            f"Error fetching employee data: \
            {response.status_code} {response.text}"
        )
        sys.exit(1)
    return response.json()


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


def get_list_task(tasks_data, name_employee, id_employee):
    """make lists with data"""

    list_task = []
    for dict in tasks_data:
        new_dict = {
            "username": name_employee,
            "task": dict["title"],
            "completed": dict["completed"],
        }
        list_task.append(new_dict)
    return list_task


def list_to_json(total_dict):
    """list to json file"""
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(total_dict, json_file)


def get_json_dict(employee_data):
    """save tasks in a dictionnary"""
    json_dict = {}
    for employee in employee_data:
        user_id = employee["id"]
        user_name = employee["username"]
        tasks_data = get_tasks_data(user_id)
        new_dict = get_list_task(tasks_data, user_name, user_id)
        json_dict[user_id] = new_dict
    return json_dict


def main():
    if len(sys.argv) > 1:
        print("Usage: script_name")
        sys.exit(1)

    # Retrieve employee related data
    employee_data = get_employee_data()

    # Retrieve all task by employee
    json_dict = get_json_dict(employee_data)

    # Save in json
    list_to_json(json_dict)


if __name__ == "__main__":
    main()
