#!/usr/local/bin/python3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

print ("Content-type: text/html; charset=utf-8\n\n")
print ("<html>")
print ("<head><title>Query Results</title></head>")
print ("<body><p>Hello</p></body></html>")
