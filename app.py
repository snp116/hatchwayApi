
from urllib import response
from flask import Flask, request, jsonify, render_template
import requests
import json
import os
app = Flask(__name__)

tag1 = 'tech'
tag2 = 'science'

# @app.route('api/ping', methods=['GET'])
# def ping():
#     response = requests.post(url="https://api.hatchways.io/assessment/blog/posts")
#     #"https://api.hatchways.io/assessment/blog/posts?tag=tech")
#     return json.dumps({'Success':True}), 200, {'ContentType':'application/json'}

@app.route('api/posts', methods=['GET'])
def posts():
    url = "https://api.hatchways.io/assessment/blog/posts"
    headers = {'Content-Type': 'application/json'}
    #params = 
    response = requests.get(url,params=params, headers=headers)
    data = response.json()
    dict = json.dumps(data)

    return dict

if __name__ == "__main__":
    app.run(debug=True)
