import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user = response.json()

    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()

    with open(f"{user_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[user_id, user['username'], str(task['completed']), task['title']] for task in tasks])
