#!/bin/bash
DB="db.sqlite"
MKB="mkb10.csv"
MKBO="mkbo.csv"

# Delete current base and create the new one
rm -f $DB
cat schema.sql | sqlite3 $DB

# Dump data to database from csv files
(echo .mode csv; echo .import $MKBO mkbo) | sqlite3 $DB
(echo .mode csv; echo .import $MKB mkb10) | sqlite3 $DB

# Convert empty fields to NULL value
for field in 'parent_id' 'code' 'date'; do
  echo "update mkb10 set $field = NULL where length($field) = 0;" | sqlite3 $DB
done
for field in 'parent_id' 'code'; do
  echo "update mkbo set $field = NULL where length($field) = 0;" | sqlite3 $DB
done

chmod 666 $DB
