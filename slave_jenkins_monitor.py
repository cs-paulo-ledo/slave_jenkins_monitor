#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from sys import exit
import json
#------------- Variables

#ci_api_url = 'http://ci.knowledge4.life:8080/computer/api/json'
ci_api_url = 'http://localhost:1235/computer/api/json'
slaves_required = ['njr_android_slave_new', 'njr_api_slave_new', 'njr_ios_slave' ]


#------------- Functions


#-------------------------------
def get_jenkins_api_json(url_computer_api_json):
    """docstring for get_jenkins_api_json"""
#    print("Inside in the get_jenkins_api_jso function")
    jenkins_api_json = get(url_computer_api_json)
    return(jenkins_api_json)

def get_nodes_slave(api_json_raw):
    """docstring for treating_json"""
    print("Inside in the tratando_json function")
    json_treated = api_json_raw.json()
    nodes_slave = json.dumps(json_treated)
    return(nodes_slave)

def verify_nodes_slave(nodes_slave_list):
    """verify status offline _nodes slave """
    print("Inside in the verify_nodes_slave function")
    #for node in nodes_slave_list

def main():
    """docstring for main"""
    print("Inside in the main function")
    get_jenkins_api_json(ci_api_url)

if __name__ == "__main__":
    exit(main())
