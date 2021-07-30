from lxml import etree
from ncclient import manager
from pprint import pprint
import xml.dom.minidom
import xmltodict
import sys
import json
from datetime import datetime
time = datetime.now().strftime('%Y-%m-%d_%H-%M')

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
    show = Show_Filters()
    print("\n\nCSR1000 SHOW CONFIGURE PAGE")
    print("\n" + "-" * 92)
    print("| SHOW MENU -> Select Your Desired Option" + ' ' * 50 + '|' + "\n|" + ' ' * 90 + '|' 
    "\n|   1. Show Running  2. Show Interface  3. Show Routing  4. Show System  5. Back to Main   |")
    print("-" * 92)

    while True:
        option = input("Please Enter the Number of option (1-5): ")
        if option.isdigit() and 1 <= int(option) <= 5:
            if option == "1":
                show.get_run()
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
    show = Show_Filters()
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
                show.get_inter()
            elif option == "2":
                show.get_gbinter()
            elif option == "3":
                print("\nShow VLAN Interface Waiting for update!")
            elif option == "4":
                show.get_lpinter()
            elif option == "5":
                show.get_ipinter()
            elif option == "6":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Show_Menu ()

def View_Show_Routing_Menu ():
    show = Show_Filters()
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
                show.get_route_all()
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
    show = Show_Filters()
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
                show.get_host()
            elif option == "2":
                show.get_user()
            elif option == "3":
                show.get_line()
            elif option == "4":
                show.get_license()
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
                View_Edit_Interface_Menu ()
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

def View_Edit_Interface_Menu ():
    edit = Edit_Filters()
    print("\n\nCSR1000 EDIT CONFIGURE PAGE")
    print("\n" + "-" * 93)
    print("| INTERFACE CONFIGURE MENU -> Select Your Desired Option" + ' ' * 36 + '|' + "\n|" + ' ' * 91+ '|' 
    "\n|   1. Create New Loopback       3. Modify Loopback Interface    5. Create VLAN Interface   |" 
    "\n|   2. Remove Current Loopback   4. Modify Gigabit Interface     6. Back to Main            |")
    print("-" * 93)

    while True:
        option = input("Please Enter the Number of option (1-5): ")
        if option.isdigit() and 1 <= int(option) <= 5:
            if option == "1":
                print("\n" + "-" * 80)
                edit.ide    = input("Input Loopback Number: ")
                edit.desc   = input("Input Loopback Description: ")
                edit.ip     = input("Input Loopback IP Address: ")
                edit.prefix = input("Input Loopback Subnet Mask: ")
                edit.post_lpinter()  # Create New loopback interface
            elif option == "2":
                print("\n" + "-" * 80)
                edit.ide = input("Input Loopback Number: ")
                edit.del_lpinter()   # Delete a Loopback interface
            elif option == "3":
                print("\n" + "-" * 80)
                edit.ide    = input("Modify Loopback Number: ")
                edit.desc   = input("New Description: ")
                edit.ip     = input("New IP Address: ")
                edit.prefix = input("New Subnet Mask: ")
                edit.put_lpinter()   # Modify a loopback interface
            elif option == "4":
                print("\n" + "-" * 80)
                edit.ide  = input("Modify Gigabit Number: ")
                edit.desc = input("New Description: ")
                edit.put_gbinter()   # Modify GB Interface Description
            elif option == "5":
                print("\n\nReturn to Main Menu !!!")
                View_Main_Menu ()
            break
        else:
           print("\n\n\nYour Input is Invalid, Try Again !!!")
           View_Edit_Menu ()


class Edit_Filters():     # String Option - Configure Data - Filter Template
    
    # def __init__(self, ide, description, ipaddress, prefix):
    #     self.ide = ide
    #     self.description = description
    #     self.ipaddress = ipaddress
    #     self.prefix = prefix

    def post_lpinter(self):    # String Option 501 - Create Loopback Interface
        netconf_edit_501 = open("e:/Github/DEVASC/2_Python_Test_Code/Word_Document/Filter_Template/netconf_edit_501_txt.txt").read()
        xml_filter_post_lpinter = netconf_edit_501.format(ide = self.ide, desc = self.desc, ip = self.ip, prefix = self.prefix)
        # edit_request(xml_filter_post_lpinter)
        print(xml_filter_post_lpinter)
        file = open("e:/Github/DEVASC/2_Python_Test_Code/Word_Document/Result_Template/{0}_output.txt".format(time), "w")
        file.write(xml_filter_post_lpinter + '\n')
        file.close()


class Show_Filters():     # String Option - Fetch Data - Filter Template

    def get_run(self):
        xml_filter_running = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_0.xml").read()
        get_request(xml_filter_running)
    
    def get_inter(self):
        xml_filter_inter   = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_101.xml").read()
        get_request(xml_filter_inter)
    
    def get_gbinter(self):
        xml_filter_gbinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_102.xml").read()
        get_request(xml_filter_gbinter)

    def get_lpinter(self):
        xml_filter_lpinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_103.xml").read()
        get_request(xml_filter_lpinter)   

    def get_ipinter(self):
        xml_filter_ipinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_104.xml").read()
        get_request(xml_filter_ipinter) 

    def get_route_all(self):
        xml_filter_router  = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_201.xml").read()
        get_request(xml_filter_router)

    def get_host(self):
        xml_filter_host    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_301.xml").read()
        get_request(xml_filter_host) 

    def get_user(self):
        xml_filter_user    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_302.xml").read()
        get_request(xml_filter_user) 

    def get_license(self):
        xml_filter_lic     = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_303.xml").read()
        get_request(xml_filter_lic)

    def get_line(self):
        xml_filter_mgmt    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_304.xml").read()
        get_request(xml_filter_mgmt)


def main():
    View_Main_Menu ()

if __name__ == '__main__':
    sys.exit(main())
