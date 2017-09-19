# Inject customer records into mcds customers table.

import pymysql

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

f = open ('../master.dat', 'r')

conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='mcds', charset='utf8mb4')
cur = conn.cursor()
cur.execute("USE mcds")

id = 1

for line in f:

    # chomp
    line = line.strip('\n')

    # explode
    row = line.split('|')

    # customer record
    name = row[COMPANY_NAME]
    loc = row[COMPANY_LOC]
    address = row[COMPANY_ADDRESS]
    cats = row[COMPANY_CATS]
    services = row[COMPANY_SERVICES]
    other = row[COMPANY_OTHER]
    comment = row[COMMENT]

    # contact record
    # contact record
    con_name = row[CONTACT_NAME]
    pos = row[CONTACT_POS]
    tel = row[CONTACT_TEL]
    email = row[CONTACT_EMAIL]

    print("Injecting record: ", name, loc)

    sql = "INSERT INTO `customers` (`name`, `loc`, `address`, `cats`, `services`, `other`, `comment`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(sql, (name, loc, address, cats, services, other, comment))

    sql = "INSERT INTO `contacts` (`firstname`, `position`, `landline`, `email`, `customer_id`) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, (con_name, pos, tel, email, id))

    # Must do this!                                                                                                                                
    conn.commit()

    id = id + 1

# Clean up!                                                                                                                                        
cur.close()
conn.close()
f.close()
print ("Records injected: ", id-1)
