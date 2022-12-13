import display as dp

passenger_clm_headers = "pname, age, trainnum, pnum, class, ticket_price, pnr, status"


def ticket_reservation(db, cursor):

    def get_fare(class_id):
        fares = [1400, 1200, 1000, 750]
        fare = fares[class_id-1]
        return fare

    def get_pnr():
        cursor.execute("SELECT pnr FROM passengers")
        pnrs = cursor.fetchall()
        if len(pnrs) == 0:
            pnr = 100
        else:
            pnr = pnrs[-1][0] + 1
        return pnr

    def traincheck(tnum):
        cursor.execute("SELECT tnum FROM trains")
        trains = cursor.fetchall()
        if (tnum,) not in trains:
            return False

    dp.op2_header()

    passenger_list = []
    amount = 0

    pnum = int(input("Enter number of passengers: "))
    trainnum = int(input("Enter train number: "))
    pnr = get_pnr()

    if traincheck(trainnum) == False:
        print("~"*60)
        print(f"No train with train number {trainnum} exists. Retry.")
        ticket_reservation(db, cursor)

    for n in range(pnum):
        print("~"*60)
        print(f"\t\t PASSENGER {n+1}")

        pname = input(f"Enter passenger {n+1} name: ")
        age = int(input(f"Enter age of passenger {n+1}: "))
        
        while True:
            print("\n 1 = AC First Class")
            print(" 2 = AC Second Class")
            print(" 3 = AC Third Class")
            print(" 4 = Sleeper")
            class_id = int(input("Select travelling class: "))

            if class_id <= 3:
                clss = "AC" + str(class_id)
                break
            elif class_id == 4:
                clss = "SLP"
                break
        fare = get_fare(class_id)
        amount += fare

        passenger = (pname, age, trainnum, clss, fare, pnr)
        passenger_list.append(passenger)

    print("~"*60)
    print("The following passenger data will be added to the database: ")
    for i in passenger_list:
        print(i)
    
    print(f"\nThe amount to be paid is INR {amount}.00")
    
    confirm = input("Continue? y/n: ").lower()
    
    if confirm == "y":
        for passenger in passenger_list:
            insert_cmd = f"INSERT INTO passengers VALUES{passenger}"
            cursor.execute(insert_cmd)
            db.commit()
        
        print("~"*60)
        print(f"\t Your PNR number is {pnr}.")
        print("~"*60)
        print("\t\t DATA INSERTED")
        print("~"*60)
    else:
        ticket_reservation(db, cursor)
        
