from io import BytesIO
import os
import mysql.connector
import requests
from os import environ
from connection import get_connection,close_connection
from flask import jsonify, request, send_file

UPLOAD_FOLDER = 'C:\\ram\\projects\\kmatrimony\\API\\uploads'


# Allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_image(profile_code, file):
    try:
        if file and allowed_file(file.filename):
        # Secure the filename and save the file
            print(file.filename)
            filename = file.filename
            print(os.path.join('uploads', filename))
            file.save(os.path.join('uploads', filename))
            return {'message':'Uploaded'}
    except (Exception) as error:
        return f"Error: {error}", 500



def get_image(profile_code):
    try:
        # Connect to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Query the database for the image
        cursor.execute("SELECT image FROM profile_image WHERE profile_code = %s", (profile_code,))
        image = cursor.fetchone()

        if image is None:
            return 'Image not found', 404
        
        # Convert the binary data back to an image
        image_name, image_data = image
        cursor.close()
        connection.close()

        # Send the image to the client
        return send_file(BytesIO(image_data), attachment_filename=image_name, mimetype='image/jpeg')

    except (Exception) as error:
        return f"Error: {error}", 500

