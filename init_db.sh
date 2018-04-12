#!/bin/bash
DB="db.sqlite"
FILE="mkb10.csv"

rm $DB
chmod 666 $DB

cat schema.sql | sqlite3 $DB
(echo .mode csv; echo .import $FILE mkb10) | sqlite3 $DB
for field in 'id_parent_id' 'code' 'date'; do
  echo "update mkb10 set $field = NULL where length($field) = 0;" | sqlite3 $DB
done
