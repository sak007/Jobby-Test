from importlib.machinery import SourceFileLoader
helper = SourceFileLoader('helper', 'code/Scraper/helper.py').load_module()


def test_db_connect(mocker):
    class mock_connection:
        def __init__(self, host, database, user, password):
            pass

        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return []

    mocker.patch.object(helper.mysql.connector, 'connect', mock_connection)
    connection = helper.db_connect()
    assert type(connection) == mock_connection


def test_get_all_skills(mocker):
    skills = [('Java'), ('Python'), ('C++')]

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return skills

    mocker.patch.object(helper, 'db_connect', mock_connection)

    allskills = helper.get_all_skills()

    for s in skills:
        assert s[0] in allskills


def test_get_all_skills_empty_list(mocker):
    skills = []

    class mock_connection:
        def cursor(a):
            return mock_cursor

    class mock_cursor:
        def execute(a):
            pass

        def fetchall():
            return skills

    mocker.patch.object(helper, 'db_connect', mock_connection)
    allskills = helper.get_all_skills()

    assert allskills == []


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
