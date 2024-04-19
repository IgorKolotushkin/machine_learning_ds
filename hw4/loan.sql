SELECT loan.id_client, count(loan.id_loan), sum(dcl.closed_fl) as cnt FROM d_loan as loan
                      JOIN d_close_loan dcl on loan.id_loan = dcl.id_loan
GROUP BY loan.id_client