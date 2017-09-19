#!/usr/bin/env python3

import os
import pymysql
import sys
import cgi
import cgitb

DEBUG_MODE = True

if DEBUG_MODE:
    cgitb.enable()

conn, cur = open_database()    
    
form = cgi.FieldStorage()

# TODO: Needs rewriting - need to check for SQL Injection attacks
# TODO: Queries using LIKE need to be fixed (need tables for locs, cats, services)
if "type" in form:
    query_type = form.getvalue('type')
    query_value = form.getvalue('value')     
    if query_type == "cat":
        query = "SELECT id, name, loc, cats, services FROM customers where cats like %s;"
    elif query_type == "loc":
        query = "SELECT id, name, loc, cats, services FROM customers where loc like %s;"    
    elif query_type == "service":
        query = "SELECT id, name, loc, cats, services FROM customers where services like %s;"    
    elif query_type == "BIGMAC":
        query = "SELECT id, name, loc, cats, services FROM customers;"    
        query_value = "" # Doesn't have a value
else:
    query_value = form.getvalue('company_name')
    query = "SELECT id, name, loc, cats, services FROM customers where name like %s;"    
    query_type = ""
    
query_value = "%" + query_value + "%"

if query_type == "BIGMAC":
    cur.execute(query)
else:
    cur.execute(query, query_value)

results = cur.fetchall()

header = '''
Content-type: text/html; charset=utf-8


<html>
<head><title>Query Results</title></head>
<body>
<table border='1'>
<thead>
<tr><th>ID</th><th>Company Name</th><th>Location</th><th>Categories</th><th>Services</th></tr>
</thead>
<tbody>
'''

write_out(header)

for r in results:
    write_out ("<tr>")

    # id
    write_out ("<td>{}</td>".format(r[0]))

    # name
    anchor_tag = build_anchor(r[0], r[1])
    write_out ("<td>{}</td>".format(anchor_tag))

    # loc
    write_out ("<td>{}</td>".format(r[2]))

    # cats
    write_out ("<td>{}</td>".format(r[3]))

    # services
    write_out ("<td>{}</td></tr>".format(r[4]))

    # !!! I think the std.out buffer overflows unless you do this !!!
    # Without this there's a limit on web page output that can be received
    sys.stdout.flush()

footer = '''
</tbody>
</table>
</body>
</html>
'''

write_out(footer)

close_database(conn, cur)
