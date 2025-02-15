import json
from flask import Flask,render_template, request
from read_org_master import get_org_details, validate_login, getSubscribers
from get_profiles import get_profiles,get_profile_subscriberid
from subscriber_search_profiles import match_profiles, short_list_profile
from read_ref_data import get_ref_details
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
    x=validate_login(request.get_json());    
    return make_response(jsonify(x), 200)

@app.route('/getSubscriberIds', methods=['GET', 'POST'])
def getSubscriberIds():    
    x=getSubscribers();    
    return make_response(jsonify(x), 200)

@app.route('/getprofiles', methods=['GET', 'POST'])
def getprofiles():
    #print(request.args.get('filter'))
    x=get_profiles(request.args.get('filter'));    
    return make_response(jsonify(x), 200)

@app.route('/getprofilesBySubscriberId', methods=['GET', 'POST'])
def getprofilesBySubscriberId():
    #print(request.args.get('filter'))
    x=get_profile_subscriberid(request.get_json());    
    return make_response(jsonify(x), 200)

@app.route('/matchprofiles', methods=['GET', 'POST'])
def matchprofiles():    
    print(request.get_json())
    x=match_profiles(request.get_json());    
    return make_response(jsonify(x), 200)

@app.route('/createProfile', methods=['POST'])
def createProfile():
    data = json.loads(request.data);      
    create_profile(data)    
    return make_response(jsonify({}), 200)

@app.route('/shortListProfile', methods=['POST'])
def sortListProfile():
    data = json.loads(request.data);      
    short_list_profile(data)    
    return make_response(jsonify({}), 200)

@app.route('/updateProfile', methods=['PUT'])
def updateProfile():
    data = json.loads(request.data);      
    update_profile(data)    
    return make_response(jsonify({}), 200)

@app.route('/getRef', methods=['GET', 'POST'])
def getRefDetails():
    refType = request.args.get('ref_type')
    print(refType);
    x=get_ref_details(refType);     
    return make_response(jsonify(x), 200)

if __name__ == "__main__":
 app.run()