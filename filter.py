#
# Takes a .DAT file and writes out filtered rows to another .DAT file.
# Used to filter out only cats (or potentially services) we want 
# You would then probably run write_csv.py on the output .DAT file
# to create a mailing list for import into Mailchimp
# Example use: python3 filter.py master.dat filter > subset.dat
# Note: currently only cat filters are supported
#

import sys

# Column numbers
CATS = 3

filter = sys.argv[2].upper()
f = open (sys.argv[1], 'r')

sys.stderr.write ("Building output DAT using filter >%s< ...\n" % filter)

for line in f:

    # chomp
    line = line.strip('\n')

    # explode
    line_array = line.split('|')

    if filter in line_array[CATS]:
        print (line)    

sys.stderr.write ("Done.\n")

