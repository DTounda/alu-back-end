#!/usr/bin/python3
"""Exports employee TODO list data to CSV format."""
import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, user_id)
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())

    username = user.get("username")

    todos_url = "{}/todos?userId={}".format(base_url, user_id)
    with urllib.request.urlopen(todos_url) as response:
        todos_list = json.loads(response.read().decode())

    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_list:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
