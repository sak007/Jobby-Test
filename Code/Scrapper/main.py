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
import scrapper_linkedin
import scrapper_glassdoor
#######################################################DATABASE OPERATIONS########################################################################################


############################################creating connection for database#################################
def db_connect(properties):
    properties = open('parameters.json')
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

def clean_data(connection):
    cursor = connection.cursor()
    offsafety = "SET SQL_SAFE_UPDATES = 0"
    query1 = "delete from user_resume"
    query2 = "delete from resume_skills"
    query3 = "delete from resume_master"
    query4 = "delete from user_master"
    onsafety = "SET SQL_SAFE_UPDATES = 1"
    cursor.execute(offsafety)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(onsafety)
    connection.commit()
    pass


def get_all_skills(connection):
    sql_select_Query = "select DISTINCT skill_id,skill_title from skill_master"
    cursor=connection.cursor()
    cursor.execute(sql_select_Query)
    records=cursor.fetchall()
    all_skills={}
    for row in records:
        all_skills[row[0]]=row[1]
    #print("All skills",all_skills)
    return all_skills


def get_resume_skills(connection):
    sql_select_Query2="select  resume_id,skill_id from resume_skills"
    cursor=connection.cursor()
    cursor.execute(sql_select_Query2)
    records2=cursor.fetchall()
    resume_skills={}
    for row in records2:
        if(row[0]) in resume_skills:
            resume_skills[row[0]].append(row[1])
        else:
            resume_skills[row[0]]=[row[1]]
    return resume_skills


def get_emailing_list(connection):
    email_id_list={}
    sql_select_Query3="SELECT resume_id,user_email,user_fname from user_master um join user_resume ur on um.user_id=ur.user_id"
    cursor=connection.cursor()
    cursor.execute(sql_select_Query3)
    records_email=cursor.fetchall()
    for row in records_email:
        email_id_list[row[0]]=[row[1],row[2]]
    #print("Resume id and email id",email_id_list)
    return email_id_list


if __name__ =='__main__':
    properties = open('parameters.json')
    data = json.load(properties)
    connection = db_connect(properties)
    all_skills = get_all_skills(connection)
    #print(all_skills)
    resume_skills = get_resume_skills(connection)
    #print(resume_skills)
    email_id_list = get_emailing_list(connection)
   # print(email_list)
    job_details_linkedin, final_result_linkedin = scrapper_linkedin.get_job_description("Software Engineer", 2, data, all_skills, resume_skills, connection)
    job_details = job_details_linkedin
    final_result = final_result_linkedin
    #job_details_glassdoor, final_result_glassdoor = scrapper_glassdoor.get_job_description("Software Engineer",5,False)
    #job_details = dict()
    #final_result = dict()
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print(job_details)
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print(job_details_linkedin)
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print(job_details_glassdoor)
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #job_details = job_details.update(job_details_linkedin)
    #print(job_details)
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #job_details = job_details.update(job_details_glassdoor)
    #print(job_details)
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #print("...................................")
    #final_result = final_result.update(final_result_linkedin)
    #final_result = final_result.update(final_result_glassdoor)
    #print(final_result)
    #print("\n final_result -------\n",final_result,"\n")


##########################################################EMAIL SERVICE######################################################################


 ##generating receiever email ids
port = 587
smtp_server = "smtp.gmail.com"
login = "srijas.alerts@gmail.com"
password = "SRIJASGMAILPWD"
sender = "srijas.alerts@gmail.com"
for key in final_result:
     if key in email_id_list:
         receiver = email_id_list[key][0]
         list_of_curr_links = final_result[key]
         #print(receiver)
         msg = MIMEMultipart()
         msg['From'] = sender
         msg['To'] = receiver
         msg['Subject'] = 'SRIJAS - Job List'

         body = """\n Hi """+ email_id_list[key][1] +""",\n Good News !! \n We have found """+str(len(list_of_curr_links)) +""" job that match your resume \n"""

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
              print(login,password)
              server.login(login, password)
              server.sendmail(sender, receiver, text)
              server.quit()                                                                                # tell the script to report if your message was sent or which errors need to be fixed
              print('Sent')
              clean_data(connection)
         except (gaierror, ConnectionRefusedError):
              print('Failed to connect to the server. Bad connection settings?')
         except smtplib.SMTPServerDisconnected as e:
              print('Failed to connect to the server. Wrong user/password?')
              print(str(e))
         except smtplib.SMTPException as e:
              print('SMTP error occurred: ' + str(e))
