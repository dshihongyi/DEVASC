from lxml import etree
from ncclient import manager
from pprint import pprint
import xml.dom.minidom
import xmltodict
import sys
import json

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", 
        "username": "developer", "password": "C1sco12345"}


# Function of Get request
def get_request(xmlstring):
    print("XML FILTER")
    print(xmlstring)
    print("-" * 80)
    with manager.connect(host=router["host"], port=router["port"], username=router["username"], 
                        password=router["password"], hostkey_verify=False) as device:

        get_reply = device.get(xmlstring)
        # xmlDom = xml.dom.minidom.parseString(str(get_reply))
        get_reply_dic = xmltodict.parse(get_reply.xml)["rpc-reply"]["data"]

   
    print("NETCONF RESPONSE")
    # print(xmlDom.toprettyxml(indent=" "))
    pprint(get_reply_dic)
    print("=" * 80)
    print("=" * 80)
    main()

# Function of Edit request
def edit_request(xmlstring):
    print("XML FILTER")
    print(xmlstring)
    print("-" * 80)
    with manager.connect(host=router["host"], port=router["port"], username=router["username"], 
                        password=router["password"], hostkey_verify=False) as device:

        edit_reply = device.edit_config(target='running', config=xmlstring)
        xmlDom = xml.dom.minidom.parseString(str(edit_reply))

    print("NETCONF RESPONSE")
    print(xmlDom.toprettyxml(indent=" "))
    print("=" * 80)
    print("=" * 80)
    main()


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
                Results.show_run()
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
                Results.show_inter()
            elif option == "2":
                Results.show_gbinter()
            elif option == "3":
                print("\nShow VLAN Interface Waiting for update!")
            elif option == "4":
                Results.show_lpinter()
            elif option == "5":
                Results.show_ipinter()
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
                Results.show_route_all()
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
    "\n|   1. Hostname   2. User Infomation   3. Terminal & Management    |" 
    "\n|   4. Licenses   5. Authentication    6. Back to Main             |")
    print("-" * 68)

    while True:
        option = input("Please Enter the Number of option (1-6): ")
        if option.isdigit() and 1 <= int(option) <= 6:
            if option == "1":
                Results.show_host()
            elif option == "2":
                Results.show_user()
            elif option == "3":
                Results.show_line()
            elif option == "4":
                Results.show_license()
            elif option == "5":
                print("Show AAA pending for update")
            elif option == "6":
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


# String Option - Fetch Data - Filter Template
xml_filter_running = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_0.xml").read()
xml_filter_inter   = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_101.xml").read()
xml_filter_gbinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_102.xml").read()
xml_filter_lpinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_103.xml").read()
xml_filter_ipinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_104.xml").read()
xml_filter_router  = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_201.xml").read()
xml_filter_host    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_301.xml").read()
xml_filter_user    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_302.xml").read()
xml_filter_lic     = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_303.xml").read()
xml_filter_mgmt    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_304.xml").read()

class Results():

    def show_run():
        get_request(xml_filter_running)
    
    def show_inter():
        get_request(xml_filter_inter)
    
    def show_gbinter():
        get_request(xml_filter_gbinter)

    def show_lpinter():
        get_request(xml_filter_lpinter)   

    def show_ipinter():
        get_request(xml_filter_ipinter) 

    def show_route_all():
        get_request(xml_filter_router)

    def show_host():
        get_request(xml_filter_host) 

    def show_user():
        get_request(xml_filter_user) 

    def show_license():
        get_request(xml_filter_lic)

    def show_line():
        get_request(xml_filter_mgmt)



def main():
    View_Main_Menu ()

if __name__ == '__main__':
    sys.exit(main())
