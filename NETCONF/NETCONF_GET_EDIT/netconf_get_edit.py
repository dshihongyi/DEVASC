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
        return [option]

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
            return [option]

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
            return [option]
    
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
            return [option]
        
    elif option == "5":

        print("-" * 80)
        print("\nNETCONF EDIT - INTERFACE CONFIGURE")
        print("-" * 65)
        print("""| MODIFYING Interface Configure                                 |
|   1. Create New Loopback        2. Modify Exist Loopback      |  
|   3. Remove Exist Loopback      4. Modify Gigabit Interface   |""")
        print("-" * 65)
        option = int(input("Choose your Option: ")) + 500
        print("-" * 80)
        if option == 501:
            print("\n" + "-" * 80)
            id = int(input("Input Loopback Number: "))
            desc = input("Input Loopback Description: ")
            ip = input("Input Loopback IP Address: ")
            prefix = input("Input Loopback Subnet Mask: ")
            return [option, id, desc, ip, prefix]
        # if option in getlist:
        #     return option
    
    else:
        print("INPUT WRONG VALUE!!! LET'S CHOOSE AGAIN\n")

number = options()
str_number = [str(int) for int in number]
ide = str_number[1]
desc = str_number[2]
ip = str_number[3]
prefix = str_number[4]

def result():
    if   str_number == "0":
        get_request(xml_filter_running)
    elif str_number[0] == "101":
        get_request(xml_filter_interface)
    elif str_number[0] == "102":
        get_request(xml_filter_gbinterface)
    elif str_number[0] == "103":
        get_request(xml_filter_lpinterface)
    elif str_number[0] == "104":
        get_request(xml_filter_ipinterface)
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
        edit_request(xml_filter_post_lpinterface)
    else:
        print("\nInvalid Option - Do Again!!!")
        main()




# String Option 0
xml_filter_running = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  </native>
</filter>
"""
# String Option 101
xml_filter_interface = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
  </interface>
  </native>
</filter>
"""

# String Option 102
xml_filter_gbinterface = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <GigabitEthernet> 
        </GigabitEthernet> 
    </interface>
  </native>
</filter>
"""

# String Option 103
xml_filter_lpinterface = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <Loopback>
        </Loopback>
    </interface>
  </native>
</filter>
"""

# String Option 104
xml_filter_ipinterface = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <GigabitEthernet>
            <ip>
                <address>
                </address>
            </ip>
        </GigabitEthernet> 
    </interface>
  </native>
</filter>
"""
# String Option 201
xml_filter_router = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <router>
  </router>
  </native>
</filter>
"""

# String Option 301
xml_filter_host = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <hostname>
  </hostname>
  </native>
</filter>
"""

# String Option 302
xml_filter_user = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <username>
  </username>
  </native>
</filter>
"""

# String Option 303
xml_filter_lic = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <license>
  </license>
  </native>
</filter>
"""

# String Option 304
xml_filter_mgmt = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <line>
  </line>
  </native>
</filter>
"""

# String Option 501
xml_filter_post_lpinterface = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <Loopback>
            <name>{ide}</name>
            <description>{desc}</description>
            <ip>
                <address>
                    <primary>
                        <address>{ip}</address>
                        <mask>{prefix}</mask>
                    </primary>
                </address>
            </ip>
        </Loopback>
    </interface>
  </native>
</config>
""".format(ide = ide, desc = desc, ip = ip, prefix = prefix)



def main():
    # a = options()
    # print (a[0])
    # print(type(number[0])
    result()

if __name__ == '__main__':
    sys.exit(main())
