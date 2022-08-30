import pandas as pd
import pymysql
from sqlalchemy import create_engine

from config import *


def generate_mysql() -> pymysql.Connection:
    db = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE)
    return db


def return_count(table_name: str) -> int:
    db = generate_mysql()
    cursor = db.cursor()
    cursor.execute(f"SELECT count(*) FROM {table_name}")
    count_ = cursor.fetchone()[0]
    return count_


mysql_connection_str = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
pgsql_connection_str = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}'

mysql_connection = create_engine(mysql_connection_str)
pgsql_connection = create_engine(pgsql_connection_str)

count = return_count(MYSQL_TABLE)

i, j = MYSQL_LIMIT_OFFSET
while i <= count:
    print(f'SELECT * FROM {MYSQL_TABLE} limit {i}, {j}')

    if REPLACE_x00:
        old_, new_ = REPLACE_x00
        df = pd.read_sql(f'SELECT * FROM {MYSQL_TABLE} limit {i}, {j}', con=mysql_connection).replace(old_, new_, regex=True)
    else:
        df = pd.read_sql(f'SELECT * FROM {MYSQL_TABLE} limit {i}, {j}', con=mysql_connection)

    for bool_rows in MYSQL_BOOL_TABLE_ROWS:
        df[bool_rows] = [True if ele == 1 else False for ele in df[bool_rows]]

    df.to_sql(POSTGRES_TABLE, pgsql_connection, if_exists='append', index=False)
    i += j
