#!/bin/bash

mysqldump example > example_dump.sql
mysql -e "CREATE DATABASE new_example; USE new_example; SOURCE example_dump.sql;"

mysqldump --opt --where="1 limit 100" mysql help_keyword > help_keyword_dump.sql
