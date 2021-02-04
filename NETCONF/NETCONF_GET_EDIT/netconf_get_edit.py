from lxml import etree
from ncclient import manager
import xml.dom.minidom
import sys
import json

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", 
        "username": "developer", "password": "C1sco12345"}

# loopback = {"id": "98", "desc":"mytest", "ip": "10.98.98.1", "prefix": "255.255.255.0"}

# Function of Get request
def get_request(xmlstring):
    print("XML FILTER")
    print(xmlstring)
    print("-" * 80)
    with manager.connect(host=router["host"], port=router["port"], username=router["username"], 
                        password=router["password"], hostkey_verify=False) as device:

        get_reply = device.get(xmlstring)
        xmlDom = xml.dom.minidom.parseString(str(get_reply))

   
    print("NETCONF RESPONSE")
    print(xmlDom.toprettyxml(indent=" "))
    print("=" * 80)
    print("=" * 80)

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

def options ():
    getlist = [101,102,103,104,201,202,203,204,301,302,303,304,501,502,503,504]
    print("\nWELCOME TO THE CONFIGURE PAGE")
    print("\n" + "-" * 90)
    print("""| Fecthing Data From CSR1000                                                             |
|   > 0.Show Running   > 1.Show Interface  > 2. Show Routing  > 3. Show System           |""")
    print("-" * 90)

    print("\n" + "-" * 90)
    print("""| Modifying Data From CSR1000                                                            |
|   > 5.EDIT Inteface  > 6.EDIT Routing    > 7. EDIT System   > 8. EDIT Miscellaneous    |""")
    print("-" * 90)
    option = input("Choose your Option: ")
    print("Your Option is " + str(option))

    if option == "0":
        print("-" * 80)
        print("NETCONF GET - RUNNING CONFIGURE")
        print("-" * 80)
        return [option,0,0,0,0]

    elif option == "1":
        print("-" * 80)
        print("\n > NETCONF GET - INTERFACES CONFIGURE")
        print("-" * 35)
        print("""| Fecthing INTERFACE Configure    |
|   1. General Interface          | 
|   2. Gigabit Interface          | 
|   3. Loopback Interface         | 
|   4. Interface IP Address       |""")
        print("-" * 35)
        option = int(input("Choose your Option: ")) + 100
        print("-" * 80)
        if option in getlist:
            return [option,0,0,0,0]

    elif option == "2":
        print("-" * 80)
        print("\nNETCONF GET - ROUTING CONFIGURE")
        print("-" * 42)
        print("""| Fecthing INTERFACE Configure           |
|   1. General All    2. Static Routing  |  
|   3. OSPF Routing   4. BGP Routing     |""")
        print("-" * 42)
        option = int(input("Choose your Option: ")) + 200
        print("-" * 80)
        if option in getlist:
            return [option,0,0,0,0]

    elif option == "3":
        print("-" * 80)
        print("\nNETCONF GET - SYSTEM CONFIGURE")
        print("-" * 50)
        print("""| Fecthing SYSTEM Configure                      |
|   1. Hostname       2. User Infomation         |  
|   3. License        4. Terminal & Management   |""")
        print("-" * 50)
        option = int(input("Choose your Option: ")) + 300
        print("-" * 80)
        if option in getlist:
            return [option,0,0,0,0]
        
    elif option == "5":
        print("-" * 80)
        print("\nNETCONF EDIT - INTERFACE CONFIGURE")
        print("-" * 65)
        print("""| MODIFYING Interface Configure                                 |
|   1. Create New Loopback        3. Modify Exist Loopback      |  
|   2. Remove Exist Loopback      4. Modify Gigabit Interface   |""")
        print("-" * 65)
        option = int(input("Choose your Option: ")) + 500
        print("-" * 80)
        if option == 501:
            print("\n" + "-" * 80)
            id = int(input("Input Loopback Number: "))
            desc = input("Input Loopback Description: ")
            ip = input("Input Loopback IP Address: ")
            prefix = input("Input Loopback Subnet Mask: ")
            if option in getlist:
                return [option, id, desc, ip, prefix]
        
        if option == 501:
            print("\n" + "-" * 80)
            id = int(input("Input Loopback Number: "))
            desc = input("Input Loopback Description: ")
            ip = input("Input Loopback IP Address: ")
            prefix = input("Input Loopback Subnet Mask: ")
            if option in getlist:
                return [option, id, desc, ip, prefix] 

        if option == 502:
            print("\n" + "-" * 80)
            id = int(input("Remove Loopback Number: ") or "0")
            if id == 0:
                options()
            elif option in getlist:
                return [option, id, 0,0,0]

        if option == 503:
            print("\n" + "-" * 80)
            id = int(input("Modify Loopback Number: ") or "0")
            desc = input("New Description: ")
            ip = input("New IP Address: ")
            prefix = input("New Subnet Mask: ")
            if id == 0:
                options()
            elif option in getlist:
                return [option, id, desc, ip, prefix]

        if option == 504:
            print("\n" + "-" * 80)
            id = int(input("Modify Gigabit Number: ") or "0")
            desc = input("New Description: ")
            # ip = input("New IP Address: ")
            # prefix = input("New Subnet Mask: ")
            if id == 0:
                options()
            elif option in getlist:
                return [option, id, desc, 0,0]
            
    else:
        print("INPUT WRONG VALUE!!! LET'S CHOOSE AGAIN\n")
    options()


number = options()
str_number = [str(int) for int in number]
ide = str_number[1]
desc = str_number[2]
ip = str_number[3]
prefix = str_number[4]

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

# String Option 501 - Create Loopback Interface
netconf_edit_501 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_501.xml").read()
xml_filter_post_lpinter = netconf_edit_501.format(ide = ide, desc = desc, ip = ip, prefix = prefix)

# String Option 502 - Delete Loopback Interface
netconf_edit_502 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_delete_502.xml").read()
xml_filter_del_lpinter = netconf_edit_502.format(ide = ide)

# String Option 503 - Edit Loopback Interface
netconf_edit_503 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_503.xml").read()
xml_filter_put_lpinter = netconf_edit_503.format(ide = ide, desc = desc, ip = ip, prefix = prefix)

# String Option 504 - Edit Gigabit Interface
netconf_edit_504 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_504.xml").read()
xml_filter_put_gpinter = netconf_edit_504.format(ide = ide, desc = desc)


def result():
    if   str_number[0] == "0":
        get_request(xml_filter_running)
    elif str_number[0] == "101":
        get_request(xml_filter_inter)
    elif str_number[0] == "102":
        get_request(xml_filter_gbinter)
    elif str_number[0] == "103":
        get_request(xml_filter_lpinter)
    elif str_number[0] == "104":
        get_request(xml_filter_ipinter)
    elif str_number[0] == "201":
        get_request(xml_filter_router)
    elif str_number[0] == "301":
        get_request(xml_filter_host)
    elif str_number[0] == "302":
        get_request(xml_filter_user)
    elif str_number[0] == "303":
        get_request(xml_filter_lic)
    elif str_number[0] == "304":
        get_request(xml_filter_mgmt)
    elif str_number[0] == "501":
        edit_request(xml_filter_post_lpinter)
    elif str_number[0] == "502":
        edit_request(xml_filter_del_lpinter)
    elif str_number[0] == "503":
        edit_request(xml_filter_put_lpinter)
    else:
        print("\nInvalid Option - Do Again!!!")
        main()


def main():
    result()

if __name__ == '__main__':
    sys.exit(main())
