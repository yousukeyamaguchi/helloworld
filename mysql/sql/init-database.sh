#!/usr/bin/env bash
mysql --defaults-extra-file=/etc/mysql/conf.d/my.cnf guestbook < "/docker-entrypoint-initdb.d/001-create-table.sql"

