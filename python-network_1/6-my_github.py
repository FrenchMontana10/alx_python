#!/usr/bin/python3
""" My GitHub! """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} <username> <password>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    
    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print("None")
