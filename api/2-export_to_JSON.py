#!/usr/bin/python3
""" Using the REST API jsonplaceholder """
import json
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


def get_list_task(tasks_data, name_employee, id_employee):
    """make lists with data"""
    total_dict = {}
    new_dict = {}

    total_dict = {id_employee: []}
    for dict in tasks_data:  # liste de dictionnaires
        new_dict = {
            "task": dict["title"],
            "completed": dict["completed"],
            "username": name_employee,
        }
        total_dict[id_employee].append(new_dict)

    concat_filename = str(id_employee) + ".json"
    return total_dict, concat_filename


def list_to_json(total_dict, filename):
    """list to json file"""
    with open(filename, "w") as json_file:
        json.dump(total_dict, json_file)


def main():
    if len(sys.argv) < 2:
        print("Usage: script_name employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Retrieve employee related data
    employee_data = get_employee_data(employee_id)
    name_employee = employee_data.get("username")
    id_employee = employee_data.get("id")

    # Retrieve tasks related data
    tasks_data = get_tasks_data(employee_id)

    # Format the value in json and get the filename
    format_json, filename = get_list_task(tasks_data,
                                          name_employee,
                                          id_employee)

    # Export to JSON file
    list_to_json(format_json, filename)


if __name__ == "__main__":
    main()
