#!/bin/python3

"""logintester.py: Tests if certain http login is working."""

__author__  = "Christian Glöckner"
__licence__ = "MIT"

import requests, sys, logging

def try_login(url, user, passwd):
    try:
        res = requests.get(url, auth=(user, passwd))
    except requests.exceptions.ConnectionError as error:
        return False
    return True

def log_result(result, url):
    logging.basicConfig(filename=url, filemode='a', level=logging.DEBUG)
    logging.info(result)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: logintester.py http://foobar.com myname pass1234 test.log')
    else:
        result = try_login(*sys.argv[1:4])
        log_result(result, sys.argv[4])
