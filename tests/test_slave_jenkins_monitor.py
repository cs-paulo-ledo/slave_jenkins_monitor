import pytest
from  .. import slave_jenkins_monitor

def test_get_jenkins_api_json():
    url_jenkins_json = 'http://ci.knowledge4.life:8080/computer/api/json'
    status_code = slave_jenkins_monitor.get_jenkins_api_json(url_jenkins_json)
    assert status_code.status_code == 200

def test_tratrando_json():
    """test api_json_treated funtion"""
    url_jenkins_json = 'http://ci.knowledge4.life:8080/computer/api/json'
    json_obj_jenkins = slave_jenkins_monitor.get_jenkins_api_json(url_jenkins_json)
    json_tratado = slave_jenkins_monitor.tratando_json(json_obj_jenkins)
    result_tratamento = isinstance(json_tratado, dict)
    assert result_tratamento == True
