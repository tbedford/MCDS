mysql -u root -p123456 -e"SELECT loc FROM customers;" mcds > temp1.txt
sed 1d temp1.txt > temp2.txt
sort temp2.txt > temp3.txt
uniq temp3.txt > db_locs.txt
rm temp*.txt
