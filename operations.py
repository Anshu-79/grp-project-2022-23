import mysql.connector as conn

import display as dp


train_clm_headers = "tname, tnum, AC1, AC2, AC3, slp"
passenger_clm_headers = "pname, age, trainnum, pnum, class, ticket_price, pnr, status"

raildb = conn.connect(host='localhost', user='root', password='root', database='railway')
cursor = raildb.cursor()

def get_pnr():
    cursor.execute("SELECT pnr FROM trains")
    pnrs = cursor.fetchall()
    if len(pnrs) == 0:
        pnr = 100
    else:
        pnr = pnrs[-1] + 1
    return pnr

def get_fare(class_id):
    fares = [750, 1000, 1200, 1400]
    fare = fares[class_id-1]
    return fare

def choose_operation():
    dp.menu()

    choice = input("Enter desired operation's number: ")
    if choice == '1':
        train_details()

    elif choice == '2':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6' or 'q':
        exit()
    else:
        print("INVALID INPUT! TRY AGAIN...")
        choose_operation()

def train_details():
    inputting_trains = True
    while inputting_trains:
        dp.op1_header()

        trainData = {}
        tname = input("Enter train name: ")
        tnum = int(input("Enter train number: "))
        ac1 = int(input("Enter number of AC 1 seats: "))
        ac2 = int(input("Enter number of AC 2 seats: "))
        ac3 = int(input("Enter number of AC 3 seats: "))
        slp = int(input("Enter number of sleeper seats: "))

        trainData['tname'] = tname
        trainData['tnum'] = tnum
        trainData['AC1'] = ac1
        trainData['AC2'] = ac2
        trainData['AC3'] = ac3
        trainData['slp'] = slp

        print("The following data will be added into the database:")
        print(trainData)

        data = tuple(trainData.values())

        confirm = input("Continue? y/n: ").lower()
        if confirm == 'y':
            cursor.execute(f"INSERT INTO trains({train_clm_headers}) VALUES{data}")
            raildb.commit()
            print("\t\t DATA INSERTED")
            print("#"*60)
            
            again = input("Insert more train data? y/n: ").lower()
            if again == 'y':
                pass
            else:
                inputting_trains = False
                choose_operation()

def ticket_reservation():
    pnum = int(input("Enter number of passengers: "))
    datalist = []
    amount = 0

    for n in range(pnum):
        data = {}
        pname = input("Enter passenger name: ")
        age = input("Enter age of passenger: ")
        trainnum = input("Enter train number: ")

        while True:
            print("1. AC First Class")
            print("2. AC Second Class")
            print("3. AC Third Class")
            print("4. Sleeper")
            class_id = int(input("Select travelling class: "))
            if class_id <= 3:
                clss = "AC" + str(class_id)
                break
            elif class_id == 4:
                clss = "SLP"
                break
        amount += get_fare(class_id)
        
        
        

        
        