#!/usr/bin/env bash

dropdb test_db
createdb test_db
psql -d test_db -f test_db_init.sql
python manage.py migrate
python manage.py loaddata daily_quote/fixtures/authors.json
python manage.py loaddata daily_quote/fixtures/quotes.json
