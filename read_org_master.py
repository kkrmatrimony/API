import os
import mysql.connector
import requests
from os import environ
from connection import get_connection,close_connection
# def get_connection():
#     connection = mysql.connector.connect(host=os.environ.get('KKKR_HOST'),
#                                          database=os.environ.get('KKKR_SCHEMA'),
#                                          user=os.environ.get('KKKR_USER'),
#                                          password=os.environ.get('KKKR_PASSWORD'),
#                                          port=os.environ.get('KKKR_PORT'))
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()

def get_org_details():
    try:        
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from org_master"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()  
        for row in records:
            x = {"OrgId":row[0], "OrgName":row[1]}                  
        close_connection(connection)
        return x;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
