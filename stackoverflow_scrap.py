#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, report, report_meta, Vote
from flask import session as login_session
import string
import excel
# IMPORTS FOR THIS STEP
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# IMPORTS FOR THIS STEP
import pprint
import httplib2
import json
import sqlite3
from flask import make_response
import requests

app = Flask(__name__)

APPLICATION_NAME = "skaner"

# Connect to Database and create database session
engine = create_engine('sqlite:///skanner.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# You need install :
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install BeautifulSoup - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup

@app.route('/')
def skanner():
    url = 'https://stackoverflow.com/'
    page =requests.get(url)
    page_list=  []
    #page_text= ""
    page_string = str(page)
    #x = str(page).find('google')
    str_page = str(page)
    for index in range(4):
        for char in page:
            if '<title>' in str(char):
                #return ""
                print(str(char))
            else:
                #return "i didn't found"
                print(str(char))

    projectData = []
    tag_counter = 0
    index_counter = 0
    tag_store = ""
    index_true = False
    for char in page:
        projectData.append(str(char))
    json_object = jsonify(str(projectData))


    for x in str(json_object):
        if index_true == True:
            index_counter += 1

            tag_store += x
        if len(tag_store) == 20:
            return tag_store
        if x == '<':
            index_true = True
            tag_counter = str(json_object).index(x)
            end_tag = tag_counter + len('<html>') + 2
    return str(tag_store)

        #for i in range(len(str(x))):
            #if projectData[i] == '<':
                #return projectData[i]

    #return json_object
        #if str(char) == "g":
            #return "Hello Google"
        #for title in element:
        #str_char = str(char)
        #return str(char)
        #x = str_char.find('<title>')
        #return str(x)
        #if '<title>' in str(char):
            #x = "hi"
            #return x
            #return "I Found Title element" + title_container


        #page_list.append(str(char) + "  ,")



        #return str(page_list)
    return "zero"


if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
