# grabs data from XLS file. Delimits columns by '|'. Use redirection
# to write out to file, otherwise output is to stdout

import sys

import openpyxl
from openpyxl import load_workbook

file = sys.argv[1]  # 'MCDS_MASTER.xlsx'
wb = load_workbook(filename = file)

sheet1 = wb.get_sheet_by_name('THAILAND')
sheet2 = wb.get_sheet_by_name('INTERNATIONAL')

ws = sheet1
rows = ws.rows

for row in ws.rows:
    record_string = ""    
    for cell in row:
        record_string = record_string + str(cell.value)
        record_string = record_string + "|" 

    # Remove carriage returns from within row    
    record_string = record_string.replace('\n', '~')    
    
    # if column 1 and column 2 are None then ignore row
    record_array = record_string.split('|') 
    colstr1 = record_array[0].strip()
    colstr2 = record_array[1].strip()
    if not colstr1 == "None":
        if not colstr2 == "None":
            print(record_string)        
    

