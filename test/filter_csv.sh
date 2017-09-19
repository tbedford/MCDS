#!/bin/bash
# 
#
#

declare -a CATS=("FABRICATION" "MANUFACTURE" "MACHINE SHOP" "OEM" "OIL AND GAS"
    "HYDRAULICS" "INDUSTRY" "MINING" "MARINE" "SUPPLY" "CIVIL" "LOGISTIC" "CRANE" "SCAFFOLDING" "INSPECTION")

declare -a SERVICES=("NDT" "OCTG" "SOLAR" "CALIBRATION" "TANK CLEAN" "TOTE TANK" "LANOTEC" "MOLYGRAPH" "DRILLING EQP" "SEP" "SMSL" "FIBRALITE" "LIFTMATE" "TWILIGHT" "RENTAL" "SELL SUPPORT") # There is also an OTHER service, need to check how we deal with that 

EXT=".csv"

rm ./CSV/*.csv

for ((i=0; i < ${#CATS[@]}; i++)); do
    python3 write_csv.py ${CATS[i]} >  "${CATS[i]}${EXT}"
done


for ((i=0; i < ${#SERVICES[@]}; i++)); do
    python3 write_csv.py ${SERVICES[i]} >  "${SERVICES[i]}${EXT}"
done


mv *.csv ./CSV

# Check for file size 0 and delete??

exit 0

