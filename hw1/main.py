import random

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(
        database='computer_company',
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


def create_product_data():
    run_sql(
        'CREATE TABLE product (maker VARCHAR(10), model INTEGER, type VARCHAR(10))'
    )

    values = []
    for code in range(1121, 1225):
        values.append(
            f"(\'{random.choice(['A', 'B', 'C', 'D', 'E', 'G', 'U', 'Q'])}\', {code}, \'{random.choice(['PC', 'Laptop', 'Printer'])}\')"
        )
    data = ', '.join(values) + '\n'
    run_sql(f"INSERT INTO product VALUES {data}")


def create_laptop_data():
    run_sql(
        'CREATE TABLE laptop (code INTEGER, model INTEGER, speed INTEGER, ram INTEGER, '
        'hd FLOAT, screen INTEGER, price FLOAT)')

    values = []
    for code, i in enumerate(range(1121, 1225), start=1):
        values.append(
            f'({code}, {i}, {random.randrange(500, 901, 100)},'
            f' {random.randrange(32, 129, 32)}, {random.randrange(5, 21, 5)},'
            f' {random.randrange(11, 22, 1)}, {random.randrange(350, 1001, 50)})'
        )
    run_sql(f"INSERT INTO laptop VALUES {', '.join(values)}")


def create_printer_data():
    run_sql(
        'CREATE TABLE printer (code INTEGER, model INTEGER, color VARCHAR(2),'
        'type VARCHAR(10), price FLOAT)')

    values = []
    for code, i in enumerate(range(1121, 1225), start=1):
        values.append(
            f"({code}, {i}, \'{random.choice(['n', 'y'])}\', "
            f"\'{random.choice(['Laser', 'Jet', 'Matrix'])}\', {random.randrange(350, 1001, 50)})"
        )
    run_sql(f"INSERT INTO printer VALUES {', '.join(values)}")


def add_duplicate():
    conn = psycopg2.connect(
        database='computer_company',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432
    )
    cur = conn.cursor()
    for dev in ['PC', 'printer', 'laptop']:
        cur.execute(f"SELECT * FROM {dev};")
        for code, data in zip(range(105, 210), cur.fetchall()):
            new = [code]
            for n in data[1:]:
                new.append(n)
            cur.execute(f"INSERT INTO {dev} VALUES {(tuple(new))}")
            conn.commit()
    conn.close()


def main():
    create_pc_data()
    create_product_data()
    create_laptop_data()
    create_printer_data()
    add_duplicate()


if __name__ == '__main__':
    main()

