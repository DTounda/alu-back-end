#!/usr/bin/python3
"""Fetches TODO list for a given employee and exports it to a JSON file."""

import json
import requests
import sys


def export_to_json(employee_id):
    """Fetch employee tasks and write them to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Could not find user with ID {employee_id}")
        sys.exit(1)
    user = user_response.json()
    username = user.get("username")

    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    # Build the data structure
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode="w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer")
        sys.exit(1)

    export_to_json(employee_id)
