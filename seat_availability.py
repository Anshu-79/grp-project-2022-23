import display as dp
from seats import seats

def seat_available(db, cursor):
    
    dp.make_header("CHECK SEAT AVAILABILITY")

    while True:
        tnum = int(input("Enter train number: "))

        cursor.execute("SELECT tnum FROM trains")
        trains = cursor.fetchall()

        if (tnum,) not in trains:
            print(f"No train with Train Number {tnum} exists. Retry.")
            print("~"*60)
        else:
            break

    avlbl_seats = seats(tnum)

    for key in avlbl_seats:
        print(f"Number of seats available in {key} = {avlbl_seats[key]}")

    