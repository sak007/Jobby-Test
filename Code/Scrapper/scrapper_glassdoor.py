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
# ===============Database Connector Script ==============================================================
def db_connect(properties):
    import mysql.connector
    from mysql.connector import Error
    import json
    data = json.load(properties)
    server_name = data['server_name']
    user_name = data['user_name']
    password = data['password']
    db_name = data['db_name']
    connection = mysql.connector.connect(host=server_name,
                                              database=db_name,
                                              user=user_name,
                                              password=password)
    
    return connection
# ================= fetch total skills database ==========================================================
def get_total_skills(connection):
    query = "select skill_id,skill_title from skill_master"
    cursor = connection.cursor()
    cursor.execute(query)
    table = cursor.fetchall()
    final_skills = {}
    for row in table:
        final_skills[row[0]]=row[1]
    return final_skills
# ========================= fetch resume id and corresponding skills ==============================================
def get_resume_id_skills(connection):
    query1 = "select r.resume_id,r.skill_id from resume_skills r where is_active='1'"
    cursor = connection.cursor()
    cursor.execute(query1)
    records = cursor.fetchall()
    mapping_dict = {}
    for row in records:
        if row[0] in mapping_dict:
            mapping_dict[row[0]].append(row[1])
        else:
            mapping_dict[row[0]] = [row[1]]
    return mapping_dict

# ======================= fetch user email ids ==================================
def get_email_id_users(connection):
    query2 = "select r.resume_id,u.user_email,u.user_fname from user_resume r join user_master u on r.user_id=u.user_id"
    cursor = connection.cursor()
    cursor.execute(query2)
    details = cursor.fetchall()
    email_dict = {}
    for row in details:
        if row[0] in email_dict:
            email_dict[row[0]].append([row[1],row[2]])
        else:
            email_dict[row[0]] = [row[1],row[2]]
    return email_dict        

# =========================== get job description =================================================================

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
     return final_dict        


if __name__ =='__main__':
    properties = open('parameters.json')
    connection = db_connect(properties)
    final_skills = get_total_skills(connection)
   #print(final_skills)
    mapping_dict = get_resume_id_skills(connection)
    #print(mapping_dict)
    email_dict = get_email_id_users(connection)
    #print(email_dict)
    final_dict = get_job_description("Software Engineer",5,False)
    #print(final_dict)
    
    
# ================= send email to users======================================================
    
    
    total = {}
    total = ke.get_user_id_to_list_of_job_ids(mapping_dict,final_dict,connection,final_skills,threshold)
    print(total)
    port = 587
    smtp_server = "smtp.gmail.com"
    login = "srijas.alerts@gmail.com"
    password = "SRIJASGMAILPWD"
    sender = "srijas.alerts@gmail.com"
    for key in total:
        if key in email_dict:
            receiver = ''.join(email_dict[key][0])
            

            list_of_curr_links = total[key]
            print(receiver)
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = 'SRIJAS - Job List'

            body = """\n Hi """+ email_dict[key][1] +""",\n Good News !! \n We have found """+str(len(list_of_curr_links)) +""" job that match your resume \n"""

            msg.attach(MIMEText(body, 'plain'))

            temp_body =""
            html_start = """<html><head></head><body><p><ol>"""
            for link in list_of_curr_links:
                temp_body +="<li>"+ job_details[link][0] + " " + job_details[link][1] + "<a href=\""+ link + "\"> Click to Apply </a>"
            html_end= """</ol></p></body> </html>"""

            html= html_start + temp_body + html_end

            msg.attach( MIMEText(html, 'html'))

            msg.attach(MIMEText("\n\n Regards, \nTeam SRIJAS", 'plain'))
            text = msg.as_string()
            
        
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.connect(smtp_server,port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(login, password)
            server.sendmail(sender, receiver, text)
            server.quit()                                                                            
            print('Sent')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected as e:
            print('Failed to connect to the server. Wrong user/password?')
            print(str(e))
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
        

