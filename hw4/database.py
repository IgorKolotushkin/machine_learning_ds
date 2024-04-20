import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


conn = psycopg2.connect(
    database='new_db',
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port=5432
)

query = """
SELECT
    AGE,
    GENDER,
    CHILD_TOTAL,
    DEPENDANTS,
    dw.comment as socstatus_work_fl,
    dp.comment as socstatus_pens_fl,
    ds.personal_income as personal_income,
    da.agreement_rk as AGREEMENT_RK,
    da.target as TARGET,
    count(dl.id_client) as LOAN_NUM_TOTAL,
    sum(dcl.closed_fl) as LOAN_NUM_CLOSED
FROM d_clients
JOIN d_work dw on dw.id = d_clients.socstatus_work_fl
JOIN d_pens dp on dp.id = d_clients.socstatus_pens_fl
JOIN d_salary ds on d_clients.id = ds.id_client
JOIN d_agreement da on d_clients.id = da.id_client
JOIN d_loan dl on d_clients.id = dl.id_client
JOIN d_close_loan dcl on dl.id_loan = dcl.id_loan
GROUP BY AGE, GENDER, CHILD_TOTAL, DEPENDANTS, dw.comment, dp.comment, ds.personal_income, da.agreement_rk, da.target
"""

df = pd.read_sql(query, conn)

df.to_csv('client.csv')

