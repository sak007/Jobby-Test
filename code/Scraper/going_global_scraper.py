"""

Scraper for GoingGlobal

@author Rithik Jain
"""

import helper
import requests
from bs4 import BeautifulSoup
import traceback


def get_jobs(role, location, no_of_jobs_to_retrieve, all_skills, country=""):
    url = 'https://www.goinglobal.com/job-search/results?keywords={0}%2C%2C&location={1}&country={2}&sort=relevance&language'.format(
        role,
        location,
        country
    )
    url = url.replace(' ', '%20')
    k1 = requests.get(url)
    # Get the main content from the webpage to scrap
    main_content = BeautifulSoup(k1.content, 'html.parser')

    # Get the raw data of all jobs listed
    all_jobs = main_content.find_all("div", {"class": "job-search-listing"})

    jobs = []
    try:
        for i in range(len(all_jobs)):
            if no_of_jobs_to_retrieve > 0:
                raw_job_data = all_jobs[i]
                job = {}
                job["title"] = raw_job_data.h3.get_text()
                job["url"] = raw_job_data.h3.a["href"]
                job["description"] = raw_job_data.find_next("div", {"class": "job-teaser"}).get_text()
                job["company"] = raw_job_data.find_next("div", {"class": "job-meta"}).get_text()
                job["extras"] = raw_job_data.find_next("div", {"class": "job-extras"}).get_text()
                job["skills"] = helper.extract_skills(job["description"], all_skills)
                no_of_jobs_to_retrieve -= 1
                jobs.append(job)
    except Exception:
        traceback.print_exc()
    return jobs
