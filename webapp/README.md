# SOS - MCDS web app

Was done as a quick and dirty proof of concept and was fully
working. I then decided to add a full authentication system and other
features, so now work in progress, but stalled due to Real
Life. Interesting to do this from scratch, but an industrial strength
web app should use Flask or Django etc.


NOTE:

Not in a working state right now. Was just adding authentication
system, then got busy with real (paid) work.

Scripts rely on a couple of softlinks, which you will need to create:

docs -> /Library/WebServer/Documents
server -> /Library/WebServer/CGI-Executables/


TODO

- Logging system required

- authentication: need to log IP address as well as cookies: session
  check should associate a session id with an IP address (i.e. when
  the session ID is created it is associated with an ip address, to
  create an "authentication pair") - we always check the session id is
  coming from the associated IP.

- no expiry on cookies to make them "session cookies"

Write up a usage policy showing - how personal data is used and
stored and why, and also why cookies - are used

- need to have a test.html page to allow testing of cookies and
  sessions

- Create custom out function to always print out with utf-8 encoding
  write_out (str)

def write_out (s):

    sys.stdout.write (s.encode('utf-8'))
    sys.stdout.write ("\r\n".encode('utf-8'))        

- introduce user sessions
- convert index.html to login page
- tidy up code
- utf-8 issues research (python 3)
- settings file to contain mysql connection data
- create user for mysql (not root!!!)
- Use templates (maybe switch to Flask??)!

