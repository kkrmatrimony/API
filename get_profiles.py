import mysql.connector
import requests
from connection import get_connection,close_connection
def serialize(row):
    return {
        
        "email" : row.email
    }

def setQuery(scenario):
    # Match the day to predefined patterns
        match scenario:
            case "LAST7DAYSCREATION":
                query = "SELECT * FROM kkkr.profile_master where created_date >=  date_sub(curdate(),  interval 7 day)"  # Match last 7 days created records
            case "LAST10DAYSUBS":
                query = "SELECT * FROM kkkr.profile_master where subscription_end_date <=  date_add(curdate(),  interval 10 day)"  # Match subscriptions ending in next 10 days
            case _:                
                query = """select * from profile_master"""  # Default case - No filter
        return query

def get_profiles(scenario):
    try:
        connection = get_connection()
        cursor = connection.cursor()        
        sql_select_query = setQuery(scenario)       
        
        cursor.execute(sql_select_query)
        records = cursor.fetchall()       
        
        resultArray = [];
        for row in records:                     
            x = {
                "profile_source":row[0],  
                "profile_code":row[1], 
                "profile_name":row[2],
                "gendar":row[3], 
                "profile_type":row[4],
                "dob":row[5],
                "age":row[6],
                "caste_sect":row[7],  
                "subsect":row[8],
                "add_subsect":row[9], 
                "gothram":row[10],
                "star_paadam":row[11],  
                "rasi":row[12],
                "birth_time":row[13],  
                "birth_place":row[14], 
                "education":row[15],
                "occupation":row[16],
                "annual_income":row[17], 
                "job_location":row[18],
                "height":row[19],
                "weight":row[20],
                "father_detail":row[21],  
                "mother_detail":row[22], 
                "sibling_detail":row[23], 
                "contact_relation":row[24],  
                "primary_contact":row[25],
                "secondary_contact":row[26],  
                "email_id":row[27],
                "brief_detail":row[28], 
                "expectation":row[29],
                "other_info":row[30],
                "agree_inform_marriage":row[31],  
                "agree_inform_exit":row[32],
                "self_declaration":row[33],
                "created_by":row[34],
                "created_date":row[35],
                "updated_by":row[36], 
                "updated_date":row[37],
                "star":row[38],
                "age_pref_from":row[39],
                "age_pref_to":row[40],
                "height_pref_from":row[41],
                "height_pref_to":row[42], 
                "profile_for":row[43],
                "salary_currency":row[44],
                "salary_preference":row[45],
                "subscription_end_date":row[47],
                "marriage_status":row[48],
                "mother_tongue":row[49],
                "citizenship":row[50],
                "father_name":row[51],
                "mother_name":row[52],
                "job_country":row[53],
                "subscriber_id":row[54],
                }  
            resultArray.append(x)           
        close_connection(connection)
        return resultArray;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
