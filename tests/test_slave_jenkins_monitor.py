import pytest
from  .. import slave_jenkins_monitor

jenkins_url = "http://localhost:1235/computer/api/json"

def test_get_jenkins_api_json():
    url_jenkins_json = jenkins_url
    status_code = slave_jenkins_monitor.get_jenkins_api_json(url_jenkins_json)
    assert status_code.status_code == 200

def test_get_nodes_slave():
    """test api_json_treated funtion"""
    json_obj_jenkins = slave_jenkins_monitor.get_jenkins_api_json(jenkins_url)
    nodes_slave_list = slave_jenkins_monitor.get_nodes_slave(json_obj_jenkins)
    result_tratamento = isinstance(nodes_slave_list, str)
    assert result_tratamento == True
