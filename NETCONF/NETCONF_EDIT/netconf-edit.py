from os import device_encoding
from ncclient import manager
from pprint import pprint
from router_info import router
import xmltodict
import xml.dom.minidom
import datetime


config_template = open("netconf_filter.xml").read()

netconf_config = config_template.format(interface_name="GigabitEthernet2", interface_desc="chido")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)