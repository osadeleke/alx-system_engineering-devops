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
        employ_username = employ_data.get('username')

    # create holding list and dictionary
    hold_list = []
    final_dict = {}
    for value in main_dict:
        hold_dict = {}
        # check for user if it is one we need
        if value.get('userId') == user_id:
            hold_dict['task'] = value.get('title')
            hold_dict['completed'] = value.get('completed')
            hold_dict['username'] = employ_username
            hold_list.append(hold_dict)
    final_dict[user_id] = hold_list
    json_file = "{}.json".format(user_id)

    # write json to file
    with open(json_file, "w") as file:
        json.dump(final_dict, file)


if __name__ == "__main__":
    main()
