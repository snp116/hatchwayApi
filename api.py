#!/usr/bin/env python
from flask import Flask, request, abort
from flask_restful import Resource, Api
from marshmallow import Schema, fields

app = Flask(__name__)
#ping 
@app.route("/ping")
#@app.route('/', methods=['GET'])
def route1():
    pass

def route2():
    pass
app.run(debug=True)