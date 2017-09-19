# MCDS

NOTE: Quick hack done in evenings/weekends for a friend's
company. Located here simply for my future reference and to provide
examples for other Python coders. There may be snippets you can reuse.

** COMPANY SENSITIVE INFORMATION REMOVED **

(c) Copyright 2016 - 2017 Tony Bedford

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

Powered by Emacs!
----
