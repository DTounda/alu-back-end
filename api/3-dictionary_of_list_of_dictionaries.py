#!/usr/bin/python3
"""Export all employees' TODO data to a single JSON file."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    users = requests.get(base_url + "/users").json()
    todos = requests.get(base_url + "/todos").json()
    
    all_data = {}
    
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        
        user_tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        
        all_data[str(user_id)] = user_tasks
    
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
