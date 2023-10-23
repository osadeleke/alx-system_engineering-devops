#!/usr/bin/python3
"""using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import csv
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
        employ_username = employ_data.get('username')

    # count the total task and task done
    csv_data = []
    for value in main_dict:
        hold_dict = {}
        if value.get('userId') == user_id:
            hold_dict["userId"] = value.get('userId')
            hold_dict['username'] = employ_username
            hold_dict['completed'] = value.get('completed')
            hold_dict['title'] = value.get('title')
            csv_data.append(hold_dict)
    file_name = "{}.csv".format(user_id)

    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, quoting=csv.QUOTE_ALL, fieldnames=[
                                                "userId",
                                                "username",
                                                "completed",
                                                "title"])
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()
