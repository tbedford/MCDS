#
# Takes a .DAT file and writes out the records in CSV format
# Mostly used for import into Google Docs or Mailchimp
# Example use: python3 write_csv.py subset.dat > list.csv
#

import sys
import fileinput

# Column numbers
COMPANY_NAME = 0
COMPANY_LOC = 1
COMPANY_ADDRESS = 2
COMPANY_CATS = 3
COMPANY_SERVICES = 4
COMPANY_OTHER = 5

CONTACT_NAME = 6
CONTACT_POS = 7
CONTACT_TEL = 8
CONTACT_EMAIL = 9
    
COMMENT = 10

# Customize as required by adding more columns
def write_csv (row):

    sys.stdout.write ("\"" + row[COMPANY_NAME] + "\"" + ",") 
    sys.stdout.write ("\"" + row[CONTACT_NAME] + "\"" + ",") 
    sys.stdout.write ("\"" + row[CONTACT_EMAIL] + "\"" + "\n") 


# Use redirection for input
for line in fileinput.input():

    # chomp
    line = line.strip('\n')

    # explode
    line_array = line.split('|')

    # Write CSVs
    write_csv(line_array)    


