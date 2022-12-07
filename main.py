from train_details import train_details
from run_operations import run

def header():
    print("="*60)
    print("\t RAILWAY RESERVATION MANAGEMENT SYSTEM")
    print("="*60)
    print("\t\t DEVELOPED BY")
    print("\t\t Anshumaan Tanwar")
    print("\t\t Nalin Singh Chauhan")
    print("\t\t Pranav Sharma")
    print("="*60)

def menu():
    print("*"*60)
    print("\t\t RAILWAY MANAGEMENT")
    print("*"*60)
    print("1. Enter Train Details")
    print("2. Ticket Reservation")
    print("3. Ticket Cancellation")
    print("4. Display PNR status")
    print("5. Quit")
    print("*"*60)

    choice = input("Enter desired operation's number: ")
    chosen_operation = run(choice)
    if n == '1':
        train_details()
    elif n == '2':
        pass
    elif n == '2':
        pass
    elif n == '3':
        pass
    elif n == '4':
        pass
    elif n == '5':
        exit()
    else:
        print("INVALID INPUT! TRY AGAIN...")
        menu()

header()
menu()
