# MYSQL-TO-PGSQL

Script for migrating data from **Mysql** to **Postgresql**. This script clones data only for now.

Python 3.6 or greater version is required.
****
***USE IT AS YOUR OWN RISK***
****

## Install Packages

Run:

```
pip install requirements.txt
```

****

## Quick Start

Install requirements first

- Clone package
- Install requirements
- Create schema and their tables as per PGsql guidelines, while keeping as many similarities possible with old mysql. 
- Edit `config.py`
- Run `python3 main.py`

Config

- `MYSQL_HOST` = mysql ip/host address
- `MYSQL_PORT` = mysql port
- `MYSQL_USER` = mysql username
- `MYSQL_PASSWORD` = mysql password
- `MYSQL_DATABASE` = old mysql database
- `MYSQL_TABLE` = old mysql rows
- `MYSQL_BOOL_TABLE_ROWS` = pymysql returned 
- `MYSQL_LIMIT_OFFSET` = this script copies data in chunks to keep memory consumption low. Please specify start and increment value. Ex: 0, 500000


- `POSTGRES_HOST` = pgsql ip/host address
- `POSTGRES_PORT` = pgsql port
- `POSTGRES_USER` = pgsql username
- `POSTGRES_PASSWORD` = pgsql password
- `POSTGRES_DATABASE` = target pgsql database
- `POSTGRES_TABLE` = target pgsql database


- `REPLACE_x00` = mysql supports "\x00" or NUL char while PGsql doesn't. So your might script throw error if your data contains NUL char. Set this to None to ignore this, otherwise '\x00' will be replaced with space (" ")  
****

# TO-DOs

- Add schema migration
- Functions migration as well? This might be impossible.

**** 

# Issues, suggestions and contributing

If you run into any issues while using the bot or if you want to request any changes or new features, open a new issue
to let us know.

If you would like to contribute to the development and profitability of the bot, simply open a PR or let us know.
