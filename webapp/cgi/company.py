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
company_id = form.getvalue('id')

query = "SELECT id, name, loc, address, cats, services FROM customers where id=%s;"    
cur.execute(query, company_id)
r = cur.fetchone()

header = '''
Content-type: text/html; charset=utf-8


<html>
<head><title>Query Results</title></head>
<body>
<h2>Company details</h2>
<table border='1'>
<thead>
<tr><th>ID</th><th>Company Name</th><th>Location</th><th>Address</th><th>Categories</th><th>Services</th></tr>
</thead>
<tbody>
<tr>
'''

write_out (header)

# id
print ("<td>", end='\r\n', file=utf8stdout)
print(r[0], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)

# name
print ("<td>", end='\r\n', file=utf8stdout)
print(r[1], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)

# loc
print ("<td>", end='\r\n', file=utf8stdout)
print(r[2], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)

# address
print ("<td>", end='\r\n', file=utf8stdout)
print(r[3], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)

# cats
print ("<td>", end='\r\n', file=utf8stdout)
print(r[4], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)

# services
print ("<td>", end='\r\n', file=utf8stdout)
print(r[5], end='\r\n', file=utf8stdout)
print ("</td>", end='\r\n', file=utf8stdout)
print ("</tr>", end='\r\n', file=utf8stdout)


print ("</tbody>")
print ("</table>", end='\r\n', file=utf8stdout)
print("<hr/>", end='\r\n', file=utf8stdout)

# I think the std.out buffer overflows unless you do this!!!
# Without this there's a limit on web page output that can be received
sys.stdout.flush()

#
# Use company_id to look up contacts
# select id, firstname, email from contacts where customer_id=company_id;
#

query = "SELECT id, firstname, email FROM contacts WHERE customer_id=%s;" % company_id

cur.execute(query)
results = cur.fetchall()

print ("<h2>Contact details</h2>",  end='\r\n', file=utf8stdout)
print ("<table border='1'>",  end='\r\n', file=utf8stdout)
print ("<thead>",  end='\r\n', file=utf8stdout)
print ("<tr><th>Contact ID</th><th>Contact Name</th><th>Email</th></tr>",  end='\r\n', file=utf8stdout)
print ("</thead>",  end='\r\n', file=utf8stdout)
print ("<tbody>",  end='\r\n', file=utf8stdout)

for r in results:
    
    print ("<tr>", end='\r\n', file=utf8stdout)

    print ("<td>", end='\r\n', file=utf8stdout)
    print(r[0], end='\r\n', file=utf8stdout)
    print ("</td>", end='\r\n', file=utf8stdout)

    print ("<td>", end='\r\n', file=utf8stdout)
    print(r[1], end='\r\n', file=utf8stdout)
    print ("</td>", end='\r\n', file=utf8stdout)

    print ("<td>", end='\r\n', file=utf8stdout)
    print(r[2], end='\r\n', file=utf8stdout)
    print ("</td>", end='\r\n', file=utf8stdout)

    print ("<tr/>", end='\r\n', file=utf8stdout)

print ("</tbody>",  end='\r\n', file=utf8stdout)
print("</table>", end='\r\n', file=utf8stdout)
print("<hr/>", end='\r\n', file=utf8stdout)

sys.stdout.flush()

print ("</body>", end='\r\n', file=utf8stdout)
print ("</html>", end='\r\n', file=utf8stdout)

close_database(conn, cur)
