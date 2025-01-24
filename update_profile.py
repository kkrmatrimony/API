from time import strftime
from typing import KeysView
import requests
from connection import get_connection,close_connection
from sequencegen import  updateSeqNumber
from datetime import datetime
def update_profile(data):
    try:        
        connection = get_connection()
        cursor = connection.cursor()                
        currentDate =datetime.today().strftime('%Y-%m-%d')        
        cursor.execute("""UPDATE profile_master SET profile_source=%s,
                        profile_name=%s,  
                        gendar=%s,
                        profile_type=%s,  
                        dob=%s,
                        age=%s,
                        caste_sect=%s,  
                        subsect=%s,
                        add_subsect=%s, 
                        gothram=%s,
                        star_paadam=%s,  
                        rasi=%s,
                        birth_time=%s,  
                        birth_place=%s, 
                        education=%s,
                        occupation=%s,
                        annual_income=%s, 
                        job_location=%s,
                        height=%s,
                        weight=%s,
                        father_detail=%s,  
                        mother_detail=%s, 
                        sibling_detail=%s, 
                        contact_relation=%s,  
                        primary_contact=%s,
                        secondary_contact=%s,  
                        email_id=%s,
                        brief_detail=%s, 
                        expectation=%s,
                        other_info=%s,
                        agree_inform_marriage=%s,  
                        agree_inform_exit=%s,
                        self_declaration=%s,
                        star=%s,
                        age_pref_from=%s,
                        age_pref_to=%s,
                        height_pref_from=%s,
                        height_pref_to=%s,
                        created_by=%s,
                        created_date=%s, 
                        updated_by=%s,
                        updated_date=%s,
                        marriage_status=%s,
                        citizenship=%s,
                       salary_currency=%s,
                       salary_preference=%s,
                       mother_tongue=%s,
                       father_name=%s,
                       mother_name=%s,
                       profile_for=%s                     
                       where profile_code=%s""",
                       (data['profile_source'], 
                        data['profile_name'],  
                        data['gendar'],
                        data['profile_type'],  
                        data['dob'],
                        data['age'],
                        data['caste_sect'],  
                        data['subsect'],
                        data['add_subsect'], 
                        data['gothram'] ,
                        data['star_paadam'],  
                        data['rasi'],
                        data['birth_time'],  
                        data['birth_place'], 
                        data['education'],
                        data['occupation'],
                        data['annual_income'], 
                        data['job_location'],
                        data['height'],
                        data['weight'],
                        data['father_detail'],  
                        data['mother_detail'], 
                        data['sibling_detail'], 
                        data['contact_relation'],  
                        data['primary_contact'],
                        data['secondary_contact'],  
                        data['email_id'],
                        data['brief_detail'], 
                        data['expectation'],
                        data['other_info'],
                        data['agree_inform_marriage'],  
                        data['agree_inform_exit'],
                        data['self_declaration'],
                        data['star'],
                        data['age_pref_from'],
                        data['age_pref_to'],
                        data['height_pref_from'],
                        data['height_pref_to'],
                        data['created_by'],
                        currentDate, 
                        data['updated_by'],
                        currentDate, 
                        data['marriage_status'],
                        data['citizenship'],                        
                        data['salary_currency'],
                        data['salary_preference'],
                        data['mother_tongue'],
                        data['father_name'],  
                        data['mother_name'],
                        data['profile_for'],
                        data['profile_code']
                        ))              
        connection.commit();
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
        'subsect',
        'add_subsect', 
        'gothram',
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
        ]
    for key in data_map:
        if key == 'profile_code':
            data[key] = profCode            
        if not key in data:
            print(key)
            data[key]=None               
    return data     


def updateProfile():
   updateSeqNumber(1, 'PROFCODE')