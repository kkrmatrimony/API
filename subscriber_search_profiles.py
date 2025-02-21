import mysql.connector
import requests
from connection import get_connection,close_connection

def setQuery(data):    
    if data['gendar'] == 'M':   
        query = """select a.*, if(b.src_profile_code is null,"Shortlist","Delist") listkey
                from  profile_master a LEFT JOIN kkkr.profile_handshake b
                ON a.profile_code=b.tgt_profile_code 
                where a.gendar="M" and a.age >=31 and ( b.src_profile_code is null or b.src_profile_code="PROFCODE00022")"""
        return query
    else: 
        data['gendar'] == 'F'
        query = """select a.*, if(b.src_profile_code is null,"Shortlist","Delist") listkey
                    from  profile_master a LEFT JOIN kkkr.profile_handshake b
                    ON a.profile_code=b.tgt_profile_code 
                    where a.gendar="M" and a.age >=%s and ( b.src_profile_code is null or b.src_profile_code="PROFCODE00022")"""
        return query

def starMatchingProfiles(data):
    if data['gendar'] == 'M':   
        query = """select a.*, if(b.src_profile_code is null,"Shortlist","Delist") listkey,
	                c.girl_star,c.boy_star
                    from  profile_master a LEFT JOIN kkkr.profile_handshake b
                    ON a.profile_code=b.tgt_profile_code 
                    LEFT JOIN (SELECT * FROM kkkr.kkkr_matching_stars where boy_star=%s) c
                    ON a.star=c.girl_star
                    where a.gendar="F" and a.age <=%s and ( b.src_profile_code is null or b.src_profile_code=%s)
                    order by girl_star desc"""
        return query
    else: 
        data['gendar'] == 'F'
        query = """select a.*, if(b.src_profile_code is null,"Shortlist","Delist") listkey,
	                c.girl_star,c.boy_star
                    from  profile_master a LEFT JOIN kkkr.profile_handshake b
                    ON a.profile_code=b.tgt_profile_code 
                    LEFT JOIN (SELECT * FROM kkkr.kkkr_matching_stars where girl_star=%s) c
                    ON a.star=c.boy_star
                    where a.gendar="M" and a.age >=%s and ( b.src_profile_code is null or b.src_profile_code=%s)
                    order by boy_star desc"""
        return query
        
def match_profiles(data):
    try:
        print(data)
        connection = get_connection()
        cursor = connection.cursor()        
        sql_select_query = setQuery(data)       
        
        cursor.execute(sql_select_query, (data['age'],))
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
                "action":row[55]
                }  
            resultArray.append(x)           
        close_connection(connection)
        print(resultArray);
        return resultArray;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


def star_match_profiles(data):
    try:        
        connection = get_connection()
        cursor = connection.cursor()        
        sql_select_query = starMatchingProfiles(data)       
        
        cursor.execute(sql_select_query, (data['star'],data['age'],data['profile_code']))
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
                "action":row[55]
                }  
            resultArray.append(x)           
        close_connection(connection)
        print(resultArray);
        return resultArray;        
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)


def get_profile_subscriberid(data):
    try:
        subscriberId = data['subscriber_id']        
        connection = get_connection()
        cursor = connection.cursor()        
        sql_select_query = """select * from kkkr.profile_master where subscriber_id = %s"""           
        cursor.execute(sql_select_query, (subscriberId,))
        records = cursor.fetchall()       
        print(records)
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

def short_list_profile(data):
    try:        
        connection = get_connection()
        cursor = connection.cursor()                        
        cursor.execute("""INSERT INTO profile_handshake(src_profile_source, src_profile_code, tgt_profile_source, tgt_profile_code, 
                       status) VALUES (%s, %s,%s, %s,%s)""",
        (data['src_profile_source'], data['src_profile_code'], data['tgt_profile_source'],data['tgt_profile_code'], data['status']))                
        connection.commit();                  
        close_connection(connection)
         
    except (Exception) as error:
        print("Error while inserting data", error)

def remove_short_list_profile(data):
    try:        
        connection = get_connection()
        cursor = connection.cursor()
                              
        cursor.execute("""DELETE FROM kkkr.profile_handshake where src_profile_code=%s   and tgt_profile_code=%s""",
        (data['src_profile_code'], data['tgt_profile_code'],))                
        connection.commit();                  
        close_connection(connection)
         
    except (Exception) as error:
        print("Error while inserting data", error)