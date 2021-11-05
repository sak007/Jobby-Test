import pytest
import sys
import json
sys.path.append("../Code/Scrapper")
from scrapper_glassdoor import get_job_description

keyword = "Software Engineer"
num_jobs = 5
verbose = False


def test_get_job_description_1():
    final_result = get_job_description(keyword,num_jobs,verbose)
    assert final_result is not None

