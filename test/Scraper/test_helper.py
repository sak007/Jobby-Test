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


def test_extract_skills_empty_description():
    result = helper.extract_skills("", ['Java', 'C++', 'Python'])
    assert result == []


def test_extract_skills_empty_skills():
    result = helper.extract_skills("Java C++ Python", [])
    assert result == []


def test_extract_skills_empty():
    result = helper.extract_skills("", [])
    assert result == []


def test_extract_skills_with_matching():
    result = helper.extract_skills("Java C++", ["Java", "C++", "Python"])
    assert result is not None
    assert result != []
    assert "Java" in result
    assert "C++" in result
    assert "Python" not in result


def test_extract_skills_without_matching():
    result = helper.extract_skills("Windows Soft Skills", ['Java', 'C++', 'Python'])
    assert result == []


def test_matching_skills_both_empty():
    result = helper.matching_skills([], [])
    assert result == []


def test_matching_skills_first_empty():
    result = helper.matching_skills([], ['Java', 'C++', 'Python'])
    assert result == []


def test_matching_skills_second_empty():
    result = helper.matching_skills(['Java', 'C++', 'Python'], [])
    assert result == []


def test_matching_skills_with_matching():
    result = helper.matching_skills(['Java', 'C++', 'Python'], ['Java', 'Python'])
    assert result is not None
    assert result != []
    assert "Java" in result
    assert "C++" not in result
    assert "Python" in result


def test_matching_skills_without_matching():
    result = helper.matching_skills(['C++', 'Spring'], ['Java', 'Python'])
    assert result == []


def test_print_matching_skills_both_empty():
    result = helper.print_matching_skills([], [])
    assert result == ""


def test_print_matching_skills_first_empty():
    result = helper.print_matching_skills([], ['Java', 'C++', 'Python'])
    assert result == ""


def test_print_matching_skills_second_empty():
    result = helper.print_matching_skills(['Java', 'C++', 'Python'], [])
    assert result == ""


def test_print_matching_skills_with_matching():
    result = helper.print_matching_skills(['Java', 'C++', 'Python'], ['Java', 'Python'])
    assert result is not None
    assert result != ""
    assert "Java" in result
    assert "C++" not in result
    assert "Python" in result


def test_print_matching_skills_without_matching():
    result = helper.print_matching_skills(['C++', 'Spring'], ['Java', 'Python'])
    assert result == ""
