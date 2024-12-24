import mysql.connector
import requests
from connection import get_connection, close_connection

def get_last_seq():
    try:
        connection = get_connection();
        cursor = connection.cursor()
        sql_select_query = """select * from vts_seq_generator"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Printing org details", "\n")
        for row in records:
            x = {"seq_type":row[0], "org_id":row[1], "last_seq_no":row[2], "org_pad":row[3]}
            print(x);                     
        close_connection(connection)
        return x;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)