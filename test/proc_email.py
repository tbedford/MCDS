import sys

# email addresses removed - see private notes

email = "xyz@hotmail.com abc@hotmail.com"

print (email)

# We can but grab the first address (because we only store one contact per company in database right now)

email = email.strip()

if "HYPERLINK" in email: 

    temp = email.split(',')
    email = temp[0]
    email = email.replace('=HYPERLINK("mailto:', '')
    email = email.rstrip('"')
    print (email)

elif "~" in email:
    temp = email.split('~')
    email = temp[0]
    print (email)

elif " " in email:
    temp = email.split(' ')
    email = temp[0]
    print (email)





