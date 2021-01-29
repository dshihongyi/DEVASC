from pprint import pprint
import requests
import sys
import json

requests.packages.urllib3.disable_warnings()

router = {"host": "ios-xe-mgmt.cisco.com", "port": "9443", 
        "username": "developer", 
        "password": "C1sco12345"}

def post_configured_interfaces():
    #Setup URL and Router parameter
    url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface"

    #Create Payload in JSON Format

    payload = """ 
    {
    "Cisco-IOS-XE-native:Loopback": {
            "name": 401,
            "description": "RESTCONF TEST - DS2",
            "ip": {
                "address": {
                    "primary": {
                        "address": "4.4.4.4",
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
    response = requests.post(url, auth=(router['username'],router['password']), 
                headers=headers, data=payload, verify=False )
    print(response.status_code)
    if response.status_code in [200, 201, 204]:
        print("Seccussful")
    else: 
        print("False to Connect")

    return response

def get_configured_interfaces():
    #Setup URL and Router parameter
    url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"

    #Restconf Media Type
    headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(router['username'],router['password']), 
                headers=headers, verify=False )
    print(response.status_code)
    if response.status_code in [200, 202, 204]:
        print("Print output")
    else: 
        print("False to Connect")

    return response

def main():
    post = post_configured_interfaces()
    pprint(post.json())
    interfaces = get_configured_interfaces()
    print("This lookback interface has been created")
    print('*' * 50)
    pprint(interfaces.json())
    
if __name__ == '__main__':
    sys.exit(main())
    