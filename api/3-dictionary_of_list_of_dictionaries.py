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

    # Check if all users exist in output
    all_users_exist = all(user_id in data for user_id in map(str, range(1, 11)))

    # Check if all tasks are assigned to the correct user IDs
    tasks_assigned_correctly = all(all(task['username'] == users[user_id - 1]['username'] for task in data[str(user_id)]) for user_id in range(1, 11))

    print(f"All users exist in output: {all_users_exist}")
    print(f"All tasks assigned correctly: {tasks_assigned_correctly}")
