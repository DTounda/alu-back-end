#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    user_name = user.get("name")
    todos_list = requests.get("{}/todos".format(base_url),
                              params={"userId": user_id}).json()
    number_of_task = len(todos_list)
    task_completed = []
    for task in todos_list:
        if task.get("completed") is True:
            task_completed.append(task)
    total_number_of_task = len(task_completed)
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, total_number_of_task, number_of_task))
    for task in task_completed:
        print("\t {}".format(task.get("title")))
