import sys
import fileinput
from enum import Enum
from validate_email import validate_email

DEBUG_MODE=True
EMAIL_WARN_NONE = False
EMAIL_WARN_VALID = True
CAT_WARN_VALID = True
LOC_WARN_VALID = True

CAT_LIST = []
SERVICE_LIST = []
LOC_LIST = []

def load_array (filename, array):

    f = open(filename, 'r')

    for line in f:
        line = line.strip('\n')
        array.append(line)

    f.close()
    return array

CAT_LIST = load_array("./spec/cats.txt", CAT_LIST)
SERVICE_LIST = load_array("./spec/services.txt", SERVICE_LIST)
LOC_LIST = load_array("./spec/locs.txt", LOC_LIST)

# Column numbers
COMPANY_NAME = 0
COMPANY_LOC = 1
COMPANY_ADDRESS = 6
COMPANY_CATS = 7

CONTACT_NAME = 2
CONTACT_POS = 3
CONTACT_TEL = 4
CONTACT_EMAIL = 5
    
SERVICE_START = 8
SERVICE_STOP = 23
SERVICE_OTHER = 24

COMMENT = 25

class Company ():
    Name = ""
    Location = ""
    Address = ""
    Cats = ""
    Services = ""
    Other = ""

class Contact ():
    Name = ""
    Pos = ""
    Tel = ""
    Email = ""

#
# Column processors - one per column
#

def proc_company_name (name):

    name = name.upper()
    name = name.replace('.', ' ')
    name = name.replace(',', ' ')
    name = name.replace('&', ' ')
    name = name.replace('(', ' ')
    name = name.replace(')', ' ')
    name = name.replace("  ", ' ')
    name = name.strip()

    return name

def proc_company_location (locs):
    
    locs = locs.strip().upper()
    locs_array = locs.split('/')

    loc_str = ""
    for l in locs_array:
        l = l.strip()
        if l not in LOC_LIST:
            if DEBUG_MODE:
                if LOC_WARN_VALID:
                    sys.stderr.write("WARNING: Unrecognized location >%s<.\n" % l)
        loc_str = loc_str + l  + ':' 
    loc_str = loc_str.rstrip(':')    

    return loc_str

def proc_company_address (add):
    
    add = add.strip()

    return add


def proc_company_cats (cats):

    cats = cats.strip().upper()
    cats_array = cats.split(',') # TODO: Not all use comma separators 

    cat_str = ""
    for c in cats_array:
        c = c.strip()
        if c not in CAT_LIST:
            if DEBUG_MODE:
                if CAT_WARN_VALID:
                    sys.stderr.write("WARNING: Unrecognized category >%s<.\n" % c)
        cat_str = cat_str + c  + ':' 
    cat_str = cat_str.rstrip(':')    
    
    return cat_str

def proc_company_services (row):
    
    services_string = ""
    col = SERVICE_START
    for s in SERVICE_LIST:

        service = row[col].strip().upper()

        if service == "X":
            services_string = services_string + s + ':'   

        col = col + 1
    services_string = services_string.rstrip(':')

    # If there are no services we can return
    if services_string == '':
        return services_string

    # Having built the services string we now validate it
    # (slightly inefficient but easier to understand)
    
    services_array = services_string.split(':')

    for s in services_array:
        if s not in SERVICE_LIST:
            if DEBUG_MODE:
                sys.stderr.write("WARNING: Unrecognized service >%s<.\n" % s)

    return services_string

def proc_contact_name (name):

    name = name.strip().title()

    return name

def proc_contact_pos (pos):

    pos = pos.strip()

    return pos

def proc_contact_tel (tel):
    
    tel = tel.strip().replace("- ", '-').replace(" -", '-')

    return tel

# See also proc_email.py for tests
def proc_contact_email (email):

    email = email.strip()

    if "HYPERLINK" in email: 
        temp = email.split(',')
        email = temp[0]
        email = email.replace('=HYPERLINK("mailto:', '')
        email = email.rstrip('"')

    elif "," in email:
        temp = email.split(',')
        email = temp[0]
        email = email.rstrip(',')
        
    elif "~" in email:
        temp = email.split('~')
        email = temp[0]

    elif " " in email:
        temp = email.split(' ')
        email = temp[0]

    # Validate email
    if not validate_email(email):
        if DEBUG_MODE:
            if EMAIL_WARN_VALID:
                sys.stderr.write("WARNING: invalid email >%s< identified.\n" % email)

    return email

def proc_other (other):
    
    other = other.strip().upper()

    return other

def proc_comment (comment):
    
    comment = comment.strip().upper()

    return comment


# MAIN

for line in fileinput.input():

    # chomp line
    line = line.strip('\n')

    # explode line into fields
    line_array = line.split('|')

    Company.Name = proc_company_name(line_array[COMPANY_NAME])
    Company.Location = proc_company_location(line_array[COMPANY_LOC])
    Company.Address = proc_company_address(line_array[COMPANY_ADDRESS])
    Company.Cats = proc_company_cats(line_array[COMPANY_CATS])
    Company.Services = proc_company_services(line_array)                                       
    Company.Other = proc_other(line_array[SERVICE_OTHER])

    Contact.Name = proc_contact_name(line_array[CONTACT_NAME])
    Contact.Position = proc_contact_pos(line_array[CONTACT_POS])
    Contact.Telephone = proc_contact_tel(line_array[CONTACT_TEL])

    # First catch empty email address
    email = line_array[CONTACT_EMAIL].strip()


    if email == "None":
        if EMAIL_WARN_NONE:
            sys.stderr.write("WARNING: Email for %s is None!\n" % Contact.Name)
    else:
        Contact.Email = proc_contact_email(email)
    
    Comment = proc_comment(line_array[COMMENT])

    # Write out neat '|' delimited line    
    sys.stdout.write(Company.Name + "|")
    sys.stdout.write(Company.Location + "|")
    sys.stdout.write(Company.Address + "|")
    sys.stdout.write(Company.Cats + "|")
    sys.stdout.write(Company.Services + "|")
    sys.stdout.write(Company.Other + "|")

    sys.stdout.write(Contact.Name + "|")
    sys.stdout.write(Contact.Position + "|")
    sys.stdout.write(Contact.Telephone + "|")
    sys.stdout.write(Contact.Email + "|")

    sys.stdout.write(Comment + "\n")
