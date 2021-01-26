from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
import datetime

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", "username": "developer", "password": "C1sco12345"}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

    print("Connected")
    interface_netconf = m.get(netconf_filter)
    print("Getting running configure")

    interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

    # xmlDom = xml.dom.minidom.parseString(str(interface_netconf))

    pprint(interface_python)
    name = interface_python["interfaces"]["interface"]["name"]['#text']
    print(name)
    print("*" * 20)
    print("*" * 20)
    
#################################################################

    config = interface_python["interfaces"]["interface"]
    op_state = interface_python['interfaces-state']["interface"]
    today = datetime.datetime.today()

    print("Start")
    print(f"{today:%B %d, %Y}")
    print(f"Name: {config['name']['#text']}")
    print(f"Description: {config['description']}")
    print(f"Packets In: {op_state['statistics']['in-unicast-pkts']}")
    print("*" * 20)
    print("*" * 20)
    print('*' * 25 + 'Break' + '*' * 50)


    m.close_session()