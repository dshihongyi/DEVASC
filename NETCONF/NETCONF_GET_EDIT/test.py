import sys

def View_Main_Menu ():
    print("\nWELCOME TO THE CSR1000 CONFIGURE PAGE")
    print("\n" + "-" * 72)
    print("| MAIN MENU -> Select Your Desired Option" + ' ' * 30 + '|' + "\n|" + ' ' * 70 + '|' 
    "\n|   1. Show Configuration  2. Change Configuration  3. Exit Control    |")
    print("-" * 72)

    while True:
        option = input("Please Enter the Number of option (1-3): ")
        if option.isdigit() and 1 <= int(option) <= 3:
            if option == "1":
                View_Show_Menu ()
            elif option == "2":
                View_Edit_Menu ()
            elif option == "3":
                print("\nGood Bye !!!")
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Main_Menu ()


def View_Show_Menu ():
    print("\n\nCSR1000 SHOW CONFIGURE PAGE")
    print("\n" + "-" * 92)
    print("| SHOW MENU -> Select Your Desired Option" + ' ' * 50 + '|' + "\n|" + ' ' * 90 + '|' 
    "\n|   1. Show Running  2. Show Interface  3. Show Routing  4. Show System  5. Back to Main   |")
    print("-" * 92)

    while True:
        option = input("Please Enter the Number of option (1-5): ")
        if option.isdigit() and 1 <= int(option) <= 5:
            if option == "1":
                print("option equal to 1")
            elif option == "2":
                View_Show_Inter_Menu ()
            elif option == "3":
                View_Show_Routing_Menu ()
            elif option == "4":
                View_Show_System_Menu ()
            elif option == "5":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Show_Menu ()

def View_Edit_Menu ():
    print("\n\nCSR1000 EDIT CONFIGURE PAGE")
    print("\n" + "-" * 98)
    print("| EDIT MENU -> Select Your Desired Option" + ' ' * 56 + '|' + "\n|" + ' ' * 96 + '|' 
    "\n|   1. Edit Interface  2. Edit Routing  3. Edit System  4. EDIT Miscellaneous  5. Back to Main   |")
    print("-" * 98)

    while True:
        option = input("Please Enter the Number of option (1-5): ")
        if option.isdigit() and 1 <= int(option) <= 5:
            if option == "1":
                print("option equal to 1")
            elif option == "2":
                print("option equal to 2")
            elif option == "3":
                print("option equal to 3")
            elif option == "4":
                print("option equal to 4")
            elif option == "5":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Edit_Menu ()

def View_Show_Inter_Menu ():
    print("\n\nCSR1000 SHOW INTERFACE CONFIGURE PAGE")
    print("\n" + "-" * 73)
    print("| INTERFACE MENU -> Select Your Desired Option" + ' ' *26 + '|' + "\n|" + ' ' * 71+ '|' 
    "\n|   1. General Interface   2. Gigabit Interface     3. VLAN Interface   |" 
    "\n|   4. Loopback Interface  5. Interface IP Address  6. Back to Main     |")
    print("-" * 73)

    while True:
        option = input("Please Enter the Number of option (1-6): ")
        if option.isdigit() and 1 <= int(option) <= 6:
            if option == "1":
                print("option equal to 1")
            elif option == "2":
                print("option equal to 2")
            elif option == "3":
                print("option equal to 3")
            elif option == "4":
                print("option equal to 4")
            elif option == "5":
                print("option equal to 5")
            elif option == "6":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Show_Menu ()

def View_Show_Routing_Menu ():
    print("\n\nCSR1000 SHOW Routing CONFIGURE PAGE")
    print("\n" + "-" * 61)
    print("| ROUTING MENU -> Select Your Desired Option" + ' ' *16 + '|' + "\n|" + ' ' * 59+ '|' 
    "\n|   1. General All   2. Static Routing   3. OSPF Routing    |" 
    "\n|   4. BGP Routing   5. EIGRP Routing    6. Back to Main    |")
    print("-" * 61)

    while True:
        option = input("Please Enter the Number of option (1-6): ")
        if option.isdigit() and 1 <= int(option) <= 6:
            if option == "1":
                print("option equal to 1")
            elif option == "2":
                print("option equal to 2")
            elif option == "3":
                print("option equal to 3")
            elif option == "4":
                print("option equal to 4")
            elif option == "5":
                print("option equal to 5")
            elif option == "6":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Show_Menu ()

def View_Show_System_Menu ():
    print("\n\nCSR1000 SHOW System CONFIGURE PAGE")
    print("\n" + "-" * 68)
    print("| SYSTEM MENU -> Select Your Desired Option" + ' ' *24 + '|' + "\n|" + ' ' * 66+ '|' 
    "\n|   1. Hostname   2. User Infomation   4. Terminal & Management    |" 
    "\n|   5. Licenses   6. Authentication    7. Back to Main             |")
    print("-" * 68)

    while True:
        option = input("Please Enter the Number of option (1-7): ")
        if option.isdigit() and 1 <= int(option) <= 7:
            if option == "1":
                print("option equal to 1")
            elif option == "2":
                print("option equal to 2")
            elif option == "3":
                print("option equal to 3")
            elif option == "4":
                print("option equal to 4")
            elif option == "5":
                print("option equal to 5")
            elif option == "6":
                print("option equal to 6")
            elif option == "7":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Show_Menu ()


def main():
    View_Main_Menu ()

if __name__ == '__main__':
    sys.exit(main())
