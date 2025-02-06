from typing import KeysView
import requests
from connection import get_connection,close_connection
from sequencegen import getProfileId, updateSeqNumber
from datetime import datetime
def create_profile(data):
    try:        
        connection = get_connection()
        cursor = connection.cursor()
        profileIdRow = getProfileId()        
        for row in profileIdRow:
            profileCode = row[0]
            seq_no = row[1]                     
        currentDate =datetime.today().strftime('%Y-%m-%d')
        validateInputs(data, profileCode)           
        cursor.execute("""INSERT INTO profile_master(profile_source,
        profile_code, 
        profile_name,  
        gendar ,
        profile_type,  
        dob,
        age,
        caste_sect,  
        subsect ,
        add_subsect, 
        gothram ,
        star_paadam,  
        rasi,
        birth_time,  
        birth_place, 
        education,
        occupation,
        annual_income, 
        job_location,
        height,
        weight,
        father_detail,  
        mother_detail, 
        sibling_detail, 
        contact_relation,  
        primary_contact,
        secondary_contact,  
        email_id,
        brief_detail, 
        expectation,
        other_info,
        agree_inform_marriage,  
        agree_inform_exit,
        self_declaration,
        star,
        age_pref_from,
        age_pref_to,
        height_pref_from,
        height_pref_to,
        created_by,
        created_date, 
        updated_by,
        updated_date,
        marriage_status,
        mother_tongue,
        father_name,
        mother_name,
        citizenship,
        profile_for,
        salary_currency,
        salary_preference,
        job_country,
        subscriber_id) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
        %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
        %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
        %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
        %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (data['profile_source'], profileCode, data['profile_name'],data['gendar'], data['profile_type'],data['dob'], data['age'],data['caste_sect'], data['subsect'],data['add_subsect'],
        data['gothram'],data['star_paadam'],data['rasi'],data['birth_time'],data['birth_place'],data['education'],data['occupation'],data['annual_income'],data['job_location'],data['height'],
        data['weight'],data['father_detail'],data['mother_detail'],data['sibling_detail'],data['contact_relation'],data['primary_contact'],data['secondary_contact'],data['email_id'],data['brief_detail'],data['expectation'],
        data['other_info'],data['agree_inform_marriage'],data['agree_inform_exit'],data['self_declaration'],data['star'],data['age_pref_from'],data['age_pref_to'],data['height_pref_from'],data['height_pref_to'],
        data['created_by'],currentDate, data['updated_by'], currentDate, data['marriage_status'],data['mother_tongue'],
        data['father_name'],data['mother_name'], data['citizenship'],data['profile_for'],data['salary_currency'],data['salary_preference'], data['job_country'], data['subscriber_id']))                
        connection.commit();        
        updateSeqNumber(seq_no, 'PROFCODE')          
        close_connection(connection)
         
    except (Exception) as error:
        print("Error while inserting data", error)

def validateInputs(data, profCode):
    data_map = ['profile_source', 'profile_code', 
        'profile_name',  
        'gendar' ,
        'profile_type',  
        'dob',
        'age',
        'caste_sect',  
        'subsect' ,
        'add_subsect', 
        'gothram' ,
        'star_paadam',  
        'rasi',
        'birth_time',  
        'birth_place', 
        'education',
        'occupation',
        'annual_income', 
        'job_location',
        'height',
        'weight',
        'father_detail',  
        'mother_detail', 
        'sibling_detail', 
        'contact_relation',  
        'primary_contact',
        'secondary_contact',  
        'email_id',
        'brief_detail', 
        'expectation',
        'other_info',
        'agree_inform_marriage',  
        'agree_inform_exit',
        'self_declaration',
        'star',
        'age_pref_from',
        'age_pref_to',
        'height_pref_from',
        'height_pref_to',
        'created_by',
        'created_date', 
        'updated_by',
        'updated_date',
        'marriage_status',
        'mother_tongue',
        'father_name',
        'mother_name',
        'citizenship',
        'profile_for',
        'salary_currency',
        'salary_preference',
        'job_country',
        'subscriber_id'
        ]
    for key in data_map:
        if key == 'profile_code':
            data[key] = profCode            
        if not key in data:
            data[key]=None    
    return data     


def updateProfile():
   updateSeqNumber(1, 'PROFCODE')