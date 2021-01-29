from pprint import pprint
import requests
import sys
import json

requests.packages.urllib3.disable_warnings()

router = {"host": "ios-xe-mgmt.cisco.com", "port": "9443", 
        "username": "developer", 
        "password": "C1sco12345"}

def get_configured_interfaces():
    #Setup URL and Router parameter
    url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback?fields=101"

    #Create Payload in JSON Format

    payload = """ 
    {
    "Cisco-IOS-XE-native:GigabitEthernet": {
        "ip": {
            "address": {
                "primary": {
                    "address": "10.255.255.1",
                    "mask": "255.255.255.0"
                    }
                }
            }
        }
    }
    """
    #Restconf Media Type
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }
    # this statement performs a GET on the specified url
    response = requests.patch(url, auth=(router['username'],router['password']), 
                headers=headers, data=payload, verify=False )
    print(response.status_code)
    if response.status_code in [200, 202, 204]:
        print("Seccussful")
    else: 
        print("False to Connect")

    return response

def main():
    interfaces = get_configured_interfaces()
    pprint(interfaces.json())
    
if __name__ == '__main__':
    sys.exit(main())
    