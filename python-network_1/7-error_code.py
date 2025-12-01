#!/usr/bin/python3
""" 3543 """


import requests as req
import sys


if __name__ == "__main__":
    try:
        myreq = req.get(sys.argv[1])
        print(f"{myreq.text}")
    except req.HTTPError as e:
        print(e.status_code)
