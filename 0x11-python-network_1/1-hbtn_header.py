#!/usr/bin/python3
"""
this script sends a request URL and displays
a variable found in header of response
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        rep = response.getheader('X-Request-Id')
        print(rep)
