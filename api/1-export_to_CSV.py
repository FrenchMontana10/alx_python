import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user = user_response.json()
    username = user['username']

    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks = tasks_response.json()

    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            writer.writerow([user_id, username, str(task['completed']), task['title']])
