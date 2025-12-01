#!/usr/bin/python3
""" dfafsdsdf """


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {sys.argv[2]}"
    }
    response = requests.get(url, headers=headers)
    print(response.json()["id"])

