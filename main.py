import mysql.connector as conn

import display as dp
from train_details import train_details
from ticket_reservation import ticket_reservation
from cancel_ticket import cancel_ticket
from seat_availability import seat_available

raildb = conn.connect(host='localhost', user='root', password='root', database='railway')
cursor = raildb.cursor()

dp.main_header()

while True:
    chosen_op = dp.menu()

    if chosen_op == '1':
        train_details(raildb, cursor)
    elif chosen_op == '2':
        ticket_reservation(raildb, cursor)
    elif chosen_op == '3':
        cancel_ticket(raildb, cursor)
    elif chosen_op == '4':
        seat_available(raildb, cursor)
    elif chosen_op in ['5', 'q']:
        break
    else:
        print("INVALID INPUT! TRY AGAIN...")

raildb.close()