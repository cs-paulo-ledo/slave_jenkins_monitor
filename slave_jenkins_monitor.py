#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from sys import exit

#------------- Variables

ci_api_url = 'http://ci.knowledge4.life:8080/computer/api/json'



#------------- Functions

def get_jenkins_api_json(url_computer_api_json):
    """docstring for get_jenkins_api_json"""
#    print("Inside in the get_jenkins_api_jso function")
    jenkins_api_json = get(url_computer_api_json)
    return(jenkins_api_json)

def tratando_json(api_json_raw):
    """docstring for treating_json"""
    print("Inside in the tratando_json function")
    json_treated = api_json_raw.json()
    return(json_treated)

def main():
    """docstring for main"""
    print("Inside in the main function")
    get_jenkins_api_json(ci_api_url)

if __name__ == "__main__":
    exit(main())
