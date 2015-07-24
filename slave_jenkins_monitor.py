#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from sys import exit
import json
import yaml
from subprocess import check_output
from subprocess import call
from os import setpgrp
from os import seteuid
#------------- Variables

vars_config_file = {}
config_file = 'config_start_slave_jenkins'

# ------------ Class


class Slave_status(object):
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __verify_status_slave__(self):
        pass

class Handler_json(object):
    def __init__(self, json_jenkins):
        self.__dict__ = json.loads(json_jenkins)


class Start_jenkins_slave:
    def __init__(self, slave_list_for_start):
        self.list_for_startup = slave_list_for_start

    def slave_startup(self, conf_vars):
        for slave_down in self.list_for_startup:
            if str(slave_down) == conf_vars['SLAVE_NAME']:
                USER_NAME = conf_vars['SLAVE_USER']
                UID = check_output(['id', '-u', USER_NAME])
                USER_ID = int(UID)
#                os.setgid(CI_GUID)
#                os.seteuid(USER_ID)
                SLAVE_URL = str(conf_vars['SLAVE_URL'])
                WORK_DIR = conf_vars['SCRIPT_DIRECTORY']
#                DEVNULL = open(os.devnull, 'wb')
                call(['java', '-jar', 'slave.jar', '-jnlpUrl', SLAVE_URL],\
                    cwd=WORK_DIR, preexec_fn=setpgrp)
            else:
                return(False)

#------------- Functions
def parsing_conf_file(conf_file):
    with open(conf_file, 'r') as cfg_file:
        cfg = yaml.load(cfg_file)
    return(cfg)


def get_jenkins_api_json(url_computer_api_json):
    """docstring for get_jenkins_api_json"""
    jenkins_api_json = get(url_computer_api_json)
    return(jenkins_api_json)

def treated_jenkins_api_json(api_json_raw):
    """docstring for treating_json"""
    json_treated = json.dumps(api_json_raw.json())
    return(json_treated)

def verify_nodes_slave(nodes_slave_list, slaves_required_list):
    """verify status offline _nodes slave """
    slaves_down = []
    for node in nodes_slave_list:
        slave = Slave_status(node['displayName'], node['offline'])
        if slave.name in slaves_required_list and slave.status == True:
            slaves_down.append(slave.name)
    return(slaves_down)

#------------ Function Main ------------------------

def main():
    """docstring for main"""
    print("Inside in the main function")
    vars_config_file = parsing_conf_file(config_file)
    jenkins_api_json = get_jenkins_api_json(vars_config_file['CI_API_URL'])
    j_treated = treated_jenkins_api_json(jenkins_api_json)
    nodes_list_json = Handler_json(j_treated)
    list_slaves_down = verify_nodes_slave(nodes_list_json.computer, \
        vars_config_file['SLAVE_NAME'])
    slaves_for_startup = Start_jenkins_slave(list_slaves_down)
    slaves_for_startup.slave_startup(vars_config_file)

if __name__ == "__main__":
    exit(main())
