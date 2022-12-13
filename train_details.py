import display as dp

~ train_clm_headers = "tname, tnum, AC1, AC2, AC3, slp"

def train_details(db, cursor):
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

        cursor.execute("SELECT tnum FROM trains")
        trains = cursor.fetchall()

        if (tnum,) in trains:
            print("~"*60)
            print(f"Train number {tnum} already exists. Retry.")
            train_details(db, cursor)
            break

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
            cursor.execute(f"INSERT INTO trains VALUES{data}")
            db.commit()
            
            print("\t\t DATA INSERTED")
            print("~"*60)
            
            again = input("Insert more train data? y/n: ").lower()
            if again == 'y':
                pass
            else:
                inputting_trains = False
