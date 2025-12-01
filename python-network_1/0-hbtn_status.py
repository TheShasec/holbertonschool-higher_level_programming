#!/usr/bin/python3
""" dkjfasdfjlsd """


import urllib.request as ureq


with ureq.urlopen("https://intranet.hbtn.io/status") as res:
    print(res.read())
