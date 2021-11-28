import mysql.connector
import json


def db_connect():
    properties = open('parameters.json')
    data = json.load(properties)
    server_name = data['server_name']
    user_name = data['user_name']
    password = data['password']
    db_name = data['db_name']
    connection = mysql.connector.connect(host=server_name, database=db_name, user=user_name, password=password)
    return connection


def get_all_skills():
    connection = db_connect()
    sql_select_Query = "select DISTINCT skill_title from skill_master"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    all_skills = []
    for row in records:
        all_skills.append(row[0])
    return all_skills


def extract_skills(description, total_skills):
    list_of_skills_matched = []
    description = description.upper()
    desc_list = description.split(" ")
    for skill in total_skills:
        if (skill.upper() in desc_list) or ((skill.upper() + ".") in desc_list) or (skill.upper().center(1) in desc_list):
            list_of_skills_matched.append(skill)
    return list_of_skills_matched
