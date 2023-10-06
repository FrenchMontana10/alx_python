import json
import requests

if __name__ == "__main__":
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    data = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
        tasks = tasks_response.json()

        tasks_list = []

        for task in tasks:
            tasks_list.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        data[user_id] = tasks_list

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(data, file)
