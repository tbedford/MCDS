echo "Are you sure? This will drop the main database. Press Ctrl-C to abort."
cat create_database.sql | mysql -u root -p
python3 db_records_inject.py