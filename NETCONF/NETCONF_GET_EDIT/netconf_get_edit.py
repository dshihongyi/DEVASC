from lxml import etree
from ncclient import manager
import xml.dom.minidom
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
        xmlDom = xml.dom.minidom.parseString(str(get_reply))

   
    print("NETCONF RESPONSE")
    print(xmlDom.toprettyxml(indent=" "))
    print("=" * 80)
    print("=" * 80)

# Function of Edit request
def edit_request(xmlstring):
    print("XML FILTER")
    print("xmlstring")
    print("-" * 80)
    with manager.connect(router=router['host'], port=router['port'], username=router['username'],
                        password=router['password'], hostkey_verify=False, device_params={},
                        allow_agent=False, look_for_keys=False) as device:

        edit_reply = device.edit_config(target='running', config=xmlstring)
    
    print("NETCONF RESPONSE")
    print(edit_reply)
    print("=" * 80)
    print("=" * 80)

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

xml_filter_router = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <router>
  </router>
  </native>
</filter>
"""

def options ():
    listoptions = [101,102,103,104]
    print("\n" + "-" * 90)
    print("""| Fecthing Data From CSR1000                                                             |
|   > 0.Running Config  > 1.Interface_Config  > 2. Routing_Config  > 3. System_Config    |""")
    print("-" * 90)
    option = input("Choose your Option: ")
    print("Your Option is " + str(option))

    if option == "0":
        print("-" * 80)
        print("NETCONF GET - RUNNING CONFIGURE")
        print("-" * 80)
        return option

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
        if option in listoptions:
            return option

    elif option == "3":
        print("-" * 80)
        print("NETCONF GET - ROUTER CONFIGURE")
        print("-" * 80)

    else:
        print("INPUT WRONG VALUE!!! LET'S CHOOSE AGAIN\n")


def result():
    number = options()
    if   number == "0":
        get_request(xml_filter_running)
    elif number == 101:
        get_request(xml_filter_interface)
    elif number == 102:
        get_request(xml_filter_gbinterface)
    elif number == 103:
        get_request(xml_filter_lpinterface)
    elif number == 104:
        get_request(xml_filter_ipinterface)
    elif number == "2":
        get_request(xml_filter_router)
    else:
        print("\nInvalid Option - Do Again!!!")
        main()


def main():
    result()

if __name__ == '__main__':
    sys.exit(main())
