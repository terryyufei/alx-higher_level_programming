#!/usr/bin/python3
"""using the GitHub API to siplay my id"""

import sys
import requests


if __name__ == "__main__":
    # get the username and password from the command line
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API URL
    url = 'https://api.github.com/user'

    # headers for basic authentication
    headers = {'Authorization': f'Basic {username} {password}'}

    # send a GET request to the GitHub API
    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
