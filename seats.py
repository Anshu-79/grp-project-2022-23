import mysql.connector as conn

raildb = conn.connect(host='localhost', user='root', password='root', database='railway')
cursor = raildb.cursor()

def seats(tnum, clss=None):
    classes = "AC1, AC2, AC3, SLP"
    
    cursor.execute(f"SELECT {classes} FROM trains WHERE tnum = {tnum}")
    data = cursor.fetchall()[0]
    print(data)
    
    avlbl_seats = {'AC1':data[0], 'AC2':data[1], 'AC3':data[2], 'SLP':data[3]}
    if clss:
        return avlbl_seats[clss]
    else:
        return avlbl_seats


def fill_seat(tnum, clss):
    avlbl_seats = seats(tnum, clss)
    
    if avlbl_seats:
        cursor.execute(f"UPDATE trains SET {clss} = {avlbl_seats-1} WHERE tnum = {tnum}")
        raildb.commit()
    

def free_seat(tnum, clss):
    avlbl_seats = seats(tnum, clss)
    
    cursor.execute(f"UPDATE trains SET {clss} = {avlbl_seats+1} WHERE tnum = {tnum}")
    raildb.commit()
    