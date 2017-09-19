#!/bin/bash

python3 read_workbook.py MCDS_MASTER.xlsx > temp1.dat
cut -d'|' -f2- temp1.dat > temp2.dat
sed 1d temp2.dat > temp3.dat
python3 clean_data.py temp3.dat > master.dat
rm temp*.dat
