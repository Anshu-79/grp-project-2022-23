import mysql.connector as conn

raildb = conn.connect(host='localhost', user='root', password='root', database='railway')

cursor = raildb.cursor()

cursor.execute("""CREATE TABLE trains(
    tname VARCHAR(20),
    tnum INT PRIMARY KEY,
    AC1 INT,
    AC2 INT,
    AC3 INT,
    slp INT
)""")

cursor.execute("""CREATE TABLE passengers(
    pname VARCHAR(20),
    age INT,
    trainnum INT,
    class VARCHAR(3),
    ticket_price INT,
    pnr INT
    )""")

raildb.commit()
raildb.close()