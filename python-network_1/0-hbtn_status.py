#!/usr/bin/python3
""" dkjfasdfjlsd """


import urllib.request as ureq


with ureq.urlopen("https://intranet.hbtn.io/status") as res:
    print("Body response:")
    print(f"\n - type: {type(res.read())}")
    print(f"\n - content: {res.read()}")
    print(f"\n - utf8 content: {res.read().decode('utf-8')}")
