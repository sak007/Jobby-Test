import json
from importlib.machinery import SourceFileLoader
helper = SourceFileLoader('helper', 'code/Scraper/helper.py').load_module()


def test_db_connect(mocker):
    mocker.patch("builtins.open", return_value=[])
    mocker.patch.object(helper, 'json')
    helper.json.load.return_value = json.loads('{"server_name" : "srijas.cd1pfgqpboiq.us-east-1.rds.amazonaws.com", "user_name":"admin", "password": "adminadmin", "db_name": "srijas", "linked_in_pwd":"SRIJASGMAILPWD"}')
    connection = helper.db_connect()
    assert connection is not None


def test_get_all_skills(mocker):
    mocker.patch("builtins.open", return_value=[])
    mocker.patch.object(helper, 'json')
    helper.json.load.return_value = json.loads('{"server_name" : "srijas.cd1pfgqpboiq.us-east-1.rds.amazonaws.com", "user_name":"admin", "password": "adminadmin", "db_name": "srijas", "linked_in_pwd":"SRIJASGMAILPWD"}')
    allskills = helper.get_all_skills()
    print(allskills)
    assert allskills is not None
