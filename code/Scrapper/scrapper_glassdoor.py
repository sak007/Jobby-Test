# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:45:04 2021

@author: Jay
"""

from selenium import webdriver
import time
import keyword_extraction_modules as ke
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from selenium.webdriver.chrome.options import Options

final_dict = {}
threshold = 1
job_details={}


def get_job_description(keyword,num_jobs,verbose):
     options = Options()
     options.add_argument("--window-size-1920,1200")
     options.headless= True
     options.add_argument('--no-sandbox')
     options.add_argument('--disable-dev-shm-usage')
     driver  =  webdriver.Chrome (options=options,executable_path=ChromeDriverManager().install())
     url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
     driver.get(url)
     job_urls = []
     c=0
     job_buttons = driver.find_elements_by_xpath('.//a[@class = "jobLink job-search-key-1rd3saf eigr9kq1"]')  #jl for Job Listing. These are the buttons we're going to click.
     time.sleep(2)
     #print(len(job_buttons))
     for text in job_buttons:
         if text.get_attribute('href'):                       ### get all the job postings URL's
            job_urls.append(text.get_attribute('href'))
            c=c+1
            if(c>=num_jobs):
               break;

# ========== Iterate through each url and get the job description =================================
     for i in job_urls:
             time.sleep(5)
             jobs = []
             driver.get(i)
             button = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[2]')
             button.click()
             job_description = driver.find_element_by_xpath('//*[@id="JobDescriptionContainer"]/div[1]').text
             jobs.append(job_description)
             job_title=driver.find_element_by_xpath("//div[@class='css-17x2pwl e11nt52q6']").text
             company_details=driver.find_element_by_xpath("//div[@class='css-16nw49e e11nt52q1']").text
             job_details[i]=[job_title,company_details]
             #job_details[url]=["job_title","company_details"]
             final_dict[i] = job_description
     return job_details, final_dict
