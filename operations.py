import mysql.connector as conn

import display as dp

raildb = conn.connect(host='localhost', user='root', password='root', database='railway')
cursor = raildb.cursor()

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
    elif choice == '5' or 'q':
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

        clm_headers = "tname, tnum, AC1, AC2, AC3, slp"
        data = tuple(trainData.values())

        confirm = input("Continue? y/n: ").lower()
        if confirm == 'y':
            cursor.execute(f"INSERT INTO trains({clm_headers}) VALUES{data}")
            raildb.commit()
            print("\t\t DATA INSERTED")
            print("#"*60)
            
            again = input("Insert more train data? y/n: ").lower()
            if again == 'y':
                pass
            else:
                inputting_trains = False
                choose_operation()