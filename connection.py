import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
myvar = os.environ.get("USER1")
def get_connection():
    # connection = mysql.connector.connect(host=os.environ.get('KKKR_HOST'),
    #                                      database=os.environ.get('KKKR_SCHEMA'),
    #                                      user=os.environ.get('KKKR_USER'),
    #                                      password=os.environ.get('KKKR_PASSWORD'),
    #                                      port=os.environ.get('KKKR_PORT'))
    # return connection
    connection = mysql.connector.connect(host='172.232.120.164',
                                         database='kkkr',
                                         user='kkkr',
                                         password='Rln@2025mar',
                                         port='3306')
    return connection

def close_connection(connection):
    if connection:
        connection.close()