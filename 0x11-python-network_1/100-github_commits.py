#!/usr/bin/python3
"""using the GitHub API to list commits"""

import sys
import requests


if __name__ == "__main__":
    # get the repo name and owner from the command line
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repository_name)

    # limit no of pages
    params = {'per_page': 10}

    # send a GET request to the GitHub API
    response = requests.get(url, params=params)

    # parse the JSON response
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
