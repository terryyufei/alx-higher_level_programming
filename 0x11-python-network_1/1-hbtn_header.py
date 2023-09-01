#!/usr/bin/python3
"""using urllib to send requests"""

import sys
from urllib import request

if __name__ == "__main__":
    # get the URL from the command line argument
    url = sys.argv[1]

    # Make a GET request to the URL
    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
