#!/usr/bin/python3
""" fsaf """


import urllib.request as ureq 
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email":mail}
    request = ureq.Request(url,data)
    with ureq.urlopen(request) as res:
        print(res.read().decode("utf-8"))
