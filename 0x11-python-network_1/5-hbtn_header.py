#!/usr/bin/python3
"""Using request module to send a request to the URL"""


import requests
import sys


if __name__ == "__main__":
    # get the URL from the command line argument
    url = sys.argv[1]

    # Make a GET request to the URL
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
