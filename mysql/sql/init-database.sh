#!/usr/bin/env bash
mysql --defaults-extra-file=/etc/mysql/conf.d/my.cnf- test_db < "/docker-entrypoint-initdb.d/001-create-tables.sql"

