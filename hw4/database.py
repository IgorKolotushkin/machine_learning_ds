import random

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(
        database='new_db',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


def create_pc_data():
    """
    Создание и наполнение таблицы данными о PC
    :return:
    """
    run_sql(
        'CREATE TABLE PC (code INTEGER, model INTEGER, speed INTEGER, ram INTEGER, '
        'hd FLOAT, cd VARCHAR(50), price FLOAT)'
    )

    values = []
    for code, i in enumerate(range(1121, 1225), start=1):
        values.append(
            f'({code}, {i}, {random.randrange(500, 901, 100)},'
            f' {random.randrange(32, 129, 32)}, {random.randrange(5, 21, 5)},'
            f' \'{random.randrange(12, 53, 4)}x\', {random.randrange(350, 1001, 50)})'
        )
    data = ', '.join(values) + '\n'
    run_sql(f"INSERT INTO PC VALUES {data}")