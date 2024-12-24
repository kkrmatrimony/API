import json
from flask import Flask,render_template, request
from read_org_master import get_org_details
from get_profiles import get_profiles
from create_profile import create_profile, updateProfile
from flask import jsonify, make_response
from flask_cors import CORS
from dotenv import load_dotenv

from update_profile import update_profile
load_dotenv() 
app = Flask(__name__, static_folder='./web', static_url_path='/')
CORS(app)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    x=get_org_details();    
    return make_response(jsonify(x), 200)

@app.route('/getprofiles', methods=['GET', 'POST'])
def getprofiles():
    x=get_profiles();    
    return make_response(jsonify(x), 200)

@app.route('/createProfile', methods=['POST'])
def createProfile():
    data = json.loads(request.data);      
    create_profile(data)    
    return make_response(jsonify({}), 200)

@app.route('/updateProfile', methods=['PUT'])
def updateProfile():
    data = json.loads(request.data);      
    update_profile(data)    
    return make_response(jsonify({}), 200)

if __name__ == "__main__":
 app.run()