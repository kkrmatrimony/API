import os
import mysql.connector
import requests
from os import environ
from connection import get_connection,close_connection

def get_ref_details(refType):
    try:        
        connection = get_connection()
        cursor = connection.cursor()
        resultArray = [];        
        sql_select_query = "select * from vts_ref_master where ref_type = %s"
        cursor.execute(sql_select_query, (refType,))        
        records = cursor.fetchall()         
        for row in records:
            x = {"ref_type":row[0], "ref_code":row[1],"ref_desc":row[2]}
            resultArray.append(x)                   
        close_connection(connection)
        return resultArray;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
