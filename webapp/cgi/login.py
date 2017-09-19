#!/usr/bin/env python3

conn, cur = open_database()
    
form = cgi.FieldStorage()

email = form.getvalue ('email')
password = form.getvalue ('plaintext_password')     

hashedpw = hash_password (password)
if check_password (email, hashedpw, cur):
    session_id = create_session_id()
    write_session_id (email, session_id, cur)


close_database(conn, cur)


