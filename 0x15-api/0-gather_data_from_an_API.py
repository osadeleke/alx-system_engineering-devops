#!/usr/bin/python3
"""using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import sys
import urllib.request
import json


def main():
    """using this REST API, for a given employee ID
    returns information about his/her TODO list progress."""

    # setup api urls to be used
    main_api_url = 'https://jsonplaceholder.typicode.com'
    api_url = main_api_url + '/todos/'
    # sys.argv[1] is the first argument received
    api_employee = main_api_url + '/users/' + sys.argv[1]

    # check if the argument passed is an integer.
    try:
        user_id = int(sys.argv[1])
    except Exception as e:
        return

    # get api data from urls for todo
    with urllib.request.urlopen(api_url) as response:
        data = response.read().decode('utf-8')
        main_dict = json.loads(data)

    # get api data from urls for users
    with urllib.request.urlopen(api_employee) as response:
        employ_data = json.loads(response.read().decode('utf-8'))
        # employ_name = employ_data.get(name)
        employ_name = employ_data.get('name')

    # count the total task and task done
    done = 0
    total = 0
    done_tasks = []
    for value in main_dict:
        if value.get('userId') == user_id:
            total = total + 1
            if value.get('completed') == 1:
                done_tasks.append(value.get('title'))
                done = done + 1

    # print the output
    print_emp = "Employee {} is done with".format(employ_name)
    print_emp_sec = "tasks({}/{}):".format(done, total)
    print("{} {}".format(print_emp, print_emp_sec))
    for tasks in done_tasks:
        print("\t {}".format(tasks))


if __name__ == "__main__":
    main()
