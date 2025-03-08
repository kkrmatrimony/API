from io import BytesIO
import os
import mysql.connector
import requests
from os import environ
from connection import get_connection,close_connection
from flask import jsonify, request, send_file

#UPLOAD_FOLDER = 'C:\\ram\\projects\\kmatrimony\\API\\uploads'

base_dir = os.path.dirname(os.path.abspath(__file__))

# Set the relative folder path (uploads folder in this case)
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')


# Allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_image(file):
    try:        
        if file and allowed_file(file.filename):            
        # Secure the filename and save the file           
            filename = file.filename            
            file.save(os.path.join('uploads', filename))
            return {'message':'Uploaded'}
    except (Exception) as error:
        return f"Error: {error}", 500
    

def get_files(profCode):
    try:        
        # List all files in the specified directory (uploads folder)
        files = os.listdir(UPLOAD_FOLDER)
        #files = os.path.join('/uploads')
        
        # Filter out directories (only list files)
        files = [file for file in files if os.path.isfile(os.path.join(UPLOAD_FOLDER, file)) and profCode in file]
        
        # Return the list of files as JSON response
        return jsonify({'files': files}), 200
    except FileNotFoundError:
        return jsonify({'error': 'Directory not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500




