#!/usr/bin/python3
"""using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import json
import sys
import urllib.request


def main():
    """using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""

    # setup api urls to be used
    main_api_url = 'https://jsonplaceholder.typicode.com'
    api_url = main_api_url + '/todos/'
    # sys.argv[1] is the first argument received
    api_employee = main_api_url + '/users/'

    # get api data from urls for todo
    with urllib.request.urlopen(api_url) as response:
        data = response.read().decode('utf-8')
        main_dict = json.loads(data)

    # get api data from urls for users
    with urllib.request.urlopen(api_employee) as response:
        employ_data = json.loads(response.read().decode('utf-8'))

    final_dict = {}
    for emp in employ_data:
        hold_list = []
        for task in main_dict:
            hold_dict = {}
            if task.get("userId") == emp.get("id"):
                hold_dict['username'] = emp.get('username')
                hold_dict['task'] = task.get('title')
                hold_dict['completed'] = task.get('completed')
                hold_list.append(hold_dict)
        final_dict[emp.get('id')] = hold_list

    json_file = "todo_all_employees.json"

    # write json to file
    with open(json_file, "w") as file:
        json.dump(final_dict, file)


if __name__ == "__main__":
    main()
