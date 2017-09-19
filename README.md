# MCDS

NOTE: Quick hack done in evenings/weekends for a friend's oil services
company based in Thailand. 

Located here simply for my future reference and to provide
examples for other Python coders. There may be snippets you (or I) can reuse.

Basically the company wanted a bunch of contacts pulled from Excel, sorting into categorized lists, and have these contacts loaded to specific mailing lists in MailChimp. That was achieved fairly easily with Python. I only started the web app as a fun thing to do, it was not really part of the project. Best not to dwell on why someone might keep over 7,000 company contacts with mission critical data in a spreadhseet that gets emailed around. :cold_sweat:

There are a few interesting features:

* Had to handle Unicode from the outset, as Thai characters were required.
* Location are identified by LOCODES. Check the specs and hunt around for more info. This turned out to be an interesting aspect.
* The web app version (basically a CGI) threw up some interesting encoding issues (which were resolved). I have written this up but not yet uploaded. I need to add some more docs.
* You really should use a web framework like Flask!

**COMPANY SENSITIVE INFORMATION REMOVED**

_(c) Copyright 2016 - 2017 Tony Bedford_

No warranty is provided with this software - use at your own risk!!

Marketing Customer Database System (MCDS)

1. Spreadsheet manipulation tools
2. Web app

The spreadsheet tools were some hacks whipped together to process an
XLS spreadsheet containing several thousand company details. The main
purpose was to extract certain categories of companies and generate a
CSV file that could be imported into MailChimp.

The tools perform additional functions such as email address
verification, and normalization of phone numbers, names and other
info.

## Note on TSV files

Export from master as TAB separated Values File (TSV). 

Then type in Mac/Unix Terminal:

$ cut -f2,4,7,9 master.tsv | grep NDT | cut -f1-3 > ndt.tsv

It works fine, but of course because you cram multiple emails into
some fields that's a problem.


