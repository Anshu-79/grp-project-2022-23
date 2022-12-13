
def main_header():
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
    print("4. View Seat Availability")
    print("5. Quit")
    print("*"*60)

    choice = input("Enter desired operation's number: ")
    return choice

def make_header(header_text):
    print("#"*60)
    print("\t\t",header_text)
    print("#"*60)

