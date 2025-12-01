#!/usr/bin/python3
""" 3543 """


import requests as req


if __name__ == "__main__":
    try:
        myreq = req.get("https://intranet.hbtn.io/status")
        print(f"{myreq.text}")
    except requests.HTTPError as e:
        print(e.status_code)
