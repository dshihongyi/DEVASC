import requests
import json
from pprint import pprint

router = {"host": "ios-xe-mgmt.cisco.com", "port": "9443", 
        "username": "developer", 
        "password": "C1sco12345"}

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
}

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"


response = requests.get(url, headers=headers, auth=(router["username"], router["password"]), verify=False)

api_data = response.json()

print("*" * 50)
pprint(api_data['Cisco-IOS-XE-interfaces-oper:interface']['description'])
print("*" * 50)

if api_data['Cisco-IOS-XE-interfaces-oper:interface']['admin-status'] == 'if-state-up':
    print('Interface is up')