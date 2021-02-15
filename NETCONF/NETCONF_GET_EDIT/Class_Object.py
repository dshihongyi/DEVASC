from lxml import etree
from ncclient import manager
from pprint import pprint
import xml.dom.minidom
import xmltodict
import sys
import json

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", 
        "username": "developer", "password": "C1sco12345"}


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
    # main()

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
    # main()



# def put_gb():
#     edit_request(loop)



class Device():
    
    # def __init__(self, id, description, ipaddress, prefix):
    #     self.ide = id
    #     self.desc = description
    #     self.ip = ipaddress
    #     self.prefix = prefix

    # @classmethod
    def device_info(self):
        # print("\n" + "-" * 80)
        # ide = input("Input Loopback Number: ")
        # desc = input("Input Loopback Description: ")
        # ip = input("Input Loopback IP Address: ")
        # prefix = input("Input Loopback Subnet Mask: ")
        # print("test" + self.ide)
        netconf_edit_501 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_501.xml").read()
        xml_filter_post_lpinter = netconf_edit_501.format(ide = self.ide, desc = self.desc, ip = self.ip, prefix = self.prefix)
        # print(xml_filter_post_lpinter)
        edit_request(xml_filter_post_lpinter)
        # return 

# info = Device()
# info.ide = input("Input Loopback Number: ")
# info.desc = input("Input Loopback Description: ")
# info.ip = input("Input Loopback IP Address: ")
# info.prefix = input("Input Loopback Subnet Mask: ")
# loop = info.device_info()


def View_Edit_Interface_Menu ():
    info = Device()
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
                info.ide = input("Input Loopback Number: ")
                info.desc = input("Input Loopback Description: ")
                info.ip = input("Input Loopback IP Address: ")
                info.prefix = input("Input Loopback Subnet Mask: ")
                info.device_info()
            break



def main():
    View_Edit_Interface_Menu ()

if __name__ == '__main__':
    sys.exit(main())


# print(r1)
# t = info.show_full_name()
# print(t)
# print(t[0])
# print(type(t[0]))
# print1
# print(Device(self.id)