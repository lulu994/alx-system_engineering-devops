#!/usr/bin/python3

import sys
import requests

def get_employee_info(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data['name']
        return employee_name
    else:
        sys.exit(f"Error: Unable to retrieve employee information for ID {employee_id}.")

def get_todo_list_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        done_tasks = [todo for todo in todos if todo['completed']]
        total_done_tasks = len(done_tasks)
        return total_done_tasks, total_tasks, done_tasks
    else:
        sys.exit(f"Error: Unable to retrieve TODO list for employee ID {employee_id}.")

def display_employee_progress(employee_name, total_done_tasks, total_tasks, done_tasks):
    print(f"Employee {employee_name} is done with tasks ({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Error: Missing employee ID parameter. Please provide an integer ID.")
    try:
        employee_id = int(sys.argv[1])
        employee_name = get_employee_info(employee_id)
        total_done_tasks, total_tasks, done_tasks = get_todo_list_progress(employee_id)
        display_employee_progress(employee_name, total_done_tasks, total_tasks, done_tasks)
    except ValueError:
        sys.exit("Error: Employee ID must be an integer.")
