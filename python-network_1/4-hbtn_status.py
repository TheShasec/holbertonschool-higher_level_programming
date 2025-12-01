#!/usr/bin/python3
""" 3543 """


import requests as req


if __name__ == "__main__":
    myreq = req.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\n - type: {}".format(type(myreq.text)))
    print("\n - content: {}".format(myreq.text))
