#!/usr/bin/python3
"""Using sys and requests module to send a post request"""

import sys
import requests


if __name__ == "__main__":
    # get the URL from the command line
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # URL to send a POST request to
    url = "http://0.0.0.0:5000/search_user"

    # Letter must be sent in variable q
    data = {'q': letter}

    # send the POST request
    response = requests.post(url, data=data)

    try:
        # parse the response as JSON
        parsed_response = response.json()

        # check the format of JSON format
        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
