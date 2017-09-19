#!/usr/bin/env python3

#
# Contains all functions for SOS web app
# This is the SOS Operating System
#

import os
import pymysql
import sys
import cgi
import cgitb
import bcrypt
import random

DEBUG_MODE = True

if DEBUG_MODE:
    cgitb.enable()


# Was helpful for debugging Apache stdout encoding
def check_stdout_encoding ():

    if sys.stdout.encoding != 'UTF-8':
        error_str = '''
        Content-type: text/html; charset=utf-8


        <html>
        <body><h1>ERROR</h1></body>
        <h2>Encoding of stdout was not UTF-8 it was {}</h2>
        </html>
        '''.format(sys.stdout.encoding)
        print (error_str)
        exit()
    

# builds anchor tag from company id and name
def build_anchor(id, name):
    url = "http://127.0.0.1:80/cgi-bin/company.py?id=%s" % id
    anchor = '<a href="%s">%s</a>' % (url, name)
    return anchor        
        
# Support Unicode characters in web stream
# Odd one - utf-8 does not appear to be selected for non-tty type output
# in some cases !!!
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
    
def write_out (s):
    print (s, end='\r\n', file=utf8stdout)

# TODO: add error handling code    
def open_database ():

    # connect to database
    # TODO: we don't want to use root or expose password
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mcdsweb', charset='utf8mb4')
    cur = conn.cursor()
    cur.execute("USE mcds")
    
    return conn, cur

def close_database (conn, cur):
    cur.close()
    conn.close()


# hashes a plaintext password using bcrypt
# with bcrypt the hash contains the salt, so no
# need to store separately.
def hash_password (password):
    
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)

    return hash

# Checked hashed password against database
def check_password (email, hashedpw, cur):

    query = "SELECT hashedpw FROM users WHERE email = '{}';".format(email)
    cur.execute (query)
    result = cur.fetchone()

    if result == hashedpw:
        return True
    else:    
        return False

def create_session_id ():

    # generate seed from current time
    random.seed()
    rn = random.random()

    # hash random number to create session id
    # This will get stored in database for user
    id = bcrypt.hashpw(rn, bcrypt.gensalt())
    
    return id

# Store session id in database for user
def write_session_id (email, session_id, cur):

    query = "INSERT INTO sessions (session_id, email) VALUES ('{0}', '{1}');".format(session_id, email)
    cur.execute(query)    
    return True

# Retrieve the session email from the database
def get_session_id (session_id, cur):

    query = "SELECT email FROM sessions WHERE session_id = '{}';".format(session_id)
    cur.execute(query)
    email = cur.fetchone()
    return email
    
def delete_session_id (session_id):

    query = "DELETE from sessions WHERE sesssion_id = '{}';".format(session_id)
    cur.execute(query)    
    return True

# Creates a cookie string that will need to be written out
# into the web page header before Content-type
def create_session_cookie (id):

    cookie = "Set-Cookie:SessionID={}; HttpOnly\r\n".format(id) # Session cookie as no expiry set
    
    return cookie

# Read cookie from user's browser (session id)
def read_session_cookie ():

    if environ.has_key('HTTP_COOKIE'):
        for cookie in map(strip, split(environ['HTTP_COOKIE'], ';')):
            (key, value ) = split(cookie, '=');
            if key == "SessionID":
                id = value
    
    return id

