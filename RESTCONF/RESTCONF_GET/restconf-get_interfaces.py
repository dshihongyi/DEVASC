from pprint import pprint
import requests
import sys
import json

requests.packages.urllib3.disable_warnings()

router = {"host": "ios-xe-mgmt.cisco.com", "port": "9443", 
        "username": "developer", 
        "password": "C1sco12345"}

def get_configured_interfaces():
    url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"

    #Restconf Media Type
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(router['username'],router['password']), 
                headers=headers, verify=False )
    return response

def main():
    interfaces = get_configured_interfaces()
    pprint(interfaces.json())
    
if __name__ == '__main__':
    sys.exit(main())
    