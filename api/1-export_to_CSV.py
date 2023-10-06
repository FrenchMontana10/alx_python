import sys
import csv

# Assuming you have a list of tasks in this format: [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
# For example, tasks = [[2, "Antonette", False, "suscipit repellat esse quibusdam voluptatem incidunt"], ...]

def export_to_csv(user_id, tasks):
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks:
            writer.writerow(task)

if __name__ == "__main__":
    user_id = int(sys.argv[1])  # Assuming the user_id is provided as a command line argument
    # Fetch tasks for the given user_id and store them in a list

    # Assuming tasks is a list of lists, where each inner list represents a task
    # For example, tasks = [[2, "Antonette", False, "suscipit repellat esse quibusdam voluptatem incidunt"], ...]

    export_to_csv(user_id, tasks)
