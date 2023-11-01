import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the URL of the REST API with the employee ID
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            todos = response.json()

            # Get the employee's name from the first todo (assuming all todos have the same employee name)
            if todos:
                employee_name = todos[0]['name']

            # Count the number of completed tasks and total tasks
            completed_tasks = sum(1 for todo in todos if todo['completed'])
            total_tasks = len(todos)

            # Print the employee's TODO list progress
            print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

            # Print the titles of completed tasks
            for todo in todos:
                if todo['completed']:
                    print(f"\t{todo['title']}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
