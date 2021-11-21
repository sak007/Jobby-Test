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
import json

def get_job_description(keyword,no_of_jobs_to_retrieve,data, all_skills, resume_skills, connection):
    username="srijas.alerts@gmail.com"
    pwd=data['linked_in_pwd']
    no_of_jobs_to_retrieve=5
    count=0
    searchquery="Software Engineer"
    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.headless= True
    options.add_argument('--nosandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    match_threshold=1

    ################################Sign IN#################################################
    browser.get('https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    username_ip=browser.find_element_by_id('username')
    username_ip.send_keys(username)
    pwd_ip=browser.find_element_by_id('password')
    pwd_ip.send_keys(pwd)
    sign_in_button=browser.find_element_by_xpath("//button[@data-litms-control-urn='login-submit']")
    sign_in_button.click();


    ######################################################## traverse to job lisitng page #########################
    browser.get('https://www.linkedin.com/jobs/jobs-in-raleigh-nc?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0')
    weblement = WebDriverWait(browser, 10000).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'jobs-search-box-keyword-id')]"))
    )
    job_description=browser.find_element_by_xpath("//input[contains(@id,'jobs-search-box-keyword-id')]").send_keys(searchquery)
    #inserting job filter value
    search_button=browser.find_element_by_class_name("jobs-search-box__submit-button")
    search_button.click()
    time.sleep(3)#give time to load search query results

    ############################################scroll to the bottom of the page#############################################
    recentList = browser.find_elements_by_xpath("//section[@aria-label='pagination']")
    for list in recentList :
            browser.execute_script("arguments[0].scrollIntoView();", list )
    time.sleep(5)
    ####################################retrieve job links####################################################
    job_cards=browser.find_elements_by_xpath("//a[@class='disabled ember-view job-card-container__link job-card-list__title']")
    href_arr=[]
    for i in job_cards:
        href_arr.append(i.get_attribute("href"))
    #print(len(href_arr))

     ################looping through every job listing to scrape relevant data##################################

    final={}
    job_details={}
    listele=[]
    for url in href_arr:
         browser.get(url)
         time.sleep(5)
         show_more_button=browser.find_element_by_xpath("//button[contains(@aria-label,'Click to see more description')]")
         show_more_button.click()
         list_ele=browser.find_elements_by_xpath("//article//li")
         job_title=browser.find_element_by_xpath("//h1[@class='t-24 t-bold']").text
         company_details=browser.find_element_by_xpath("//span[@class='jobs-unified-top-card__subtitle-primary-grouping mr2 t-black']").find_element_by_xpath('//span[1]').text
         job_details[url]=[job_title,company_details]
        ############for each job lisitng loop through all list items and add the text######################
         data=[]
         datastr=""
         for li in list_ele:
             data.append(li.text)
         for val in data:
             datastr+=val + " "
         time.sleep(5)
         count+=1
         if(count==no_of_jobs_to_retrieve):
             break
         final[url]=datastr
         #print("------/n",final,"/n-------")


    #print(resume_skills,final,connection,all_skills,match_threshold)

    final_result=ke.get_user_id_to_list_of_job_ids(resume_skills,final,connection,all_skills,match_threshold)
    return job_details, final_result
