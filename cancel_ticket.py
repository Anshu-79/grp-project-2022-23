import display as dp
from seats import free_seat

def cancel_ticket(db, cursor):

    dp.make_header("TICKET CANCELLATION")

    pnr = int(input("Enter PNR number: "))

    cursor.execute(f"SELECT * FROM passengers WHERE pnr = {pnr}")
    data = cursor.fetchall()
    
    if len(data) == 0:
        print("No records are associated with given PNR number.")
    
    else:
        tnum = data[0][2]
        amount = 0
        classes = []
        for record in data:
            print(record)

            amount += record[4]
            classes.append(record[3])
            
        print("~"*60)

        confirm = input("The above tickets will be cancelled. Continue? y/n: ").lower()
        if confirm == 'y':
            
            cursor.execute(f"DELETE FROM passengers WHERE pnr = {pnr}")
            db.commit()
            for clss in classes:
                free_seat(tnum, clss)

            print("~"*60)
            print(f"An amount of INR {0.75 * amount} will be refunded to your account.")
            print("~"*60)
            print("\t\t TICKET CANCELLED")
            print("~"*60)
        

