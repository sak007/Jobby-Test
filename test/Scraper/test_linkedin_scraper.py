from importlib.machinery import SourceFileLoader
linkedin_scraper = SourceFileLoader('linkedin_scraper', 'code/Scraper/linkedin_scraper.py').load_module()


def test_get_jobs(mocker):
    jobs = linkedin_scraper.get_jobs("Software Engineer", "Raleigh", 10, ['Java', 'Python', 'Coding'])
    assert jobs is not None
