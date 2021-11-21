from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector
from mysql.connector import Error
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyword_extraction_modules as ke
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
import requests
from bs4 import BeautifulSoup
import json
import traceback

def get_job_description(role, location, no_of_jobs_to_retrieve,data, all_skills, resume_skills, connection):
    match_threshold=1
    url = "https://www.linkedin.com/jobs/jobs-in-"+location+"?keywords="+role+"&f_JT=F%2CP&f_E=1%2C3&position=1&pageNum=0"
    url = url.replace(' ', '%20')
    print(url)
    k1 = requests.get(url)
    # Run the beautiful soup
    soup1 = BeautifulSoup(k1.content, 'html.parser')
    # print(soup1)
    string1 = soup1.find_all("a",{"class":"base-card__full-link"})
    # print(string1[0])
    description_dict = {}
    job_role = []
    job_details={}
    try:

        for i in range(len(string1)):
            #print("Blah")
            if no_of_jobs_to_retrieve>0:
                dictionary = {}
                dictionary["Job Title"] = string1[i].get_text().replace('\n',' ').replace(' ','')
                dictionary["Job Link"] = string1[i]['href']
                job_details[dictionary["Job Link"]] = [dictionary["Job Title"], ""]
                job_role.append(string1[i].get_text().replace('\n',' ').replace(' ',''))
                no_of_jobs_to_retrieve-=1
                k = requests.get(string1[i]['href']).text
                soup=BeautifulSoup(k,'html.parser')
                # print(soup)
                str2 = soup.find_all("div", {"class" : "description__text"})
                # str2 = soup.find_all("div", {"class" : "show-more-less-html_markup"})
                if len(str2) > 0:
                    str3 = str2[0].get_text()
                    description_dict[dictionary["Job Link"]]=str3
        #print(description_dict)
        final_result=ke.get_user_id_to_list_of_job_ids(resume_skills,description_dict,connection,all_skills,match_threshold)
    except Exception as e:
        traceback.print_exc()
        final_result = {}
        job_role = []

    #print(job_role)
    #print(final_result)
    return job_details, final_result
