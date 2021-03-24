import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandboxsdwan.cisco.com:8443/j_security_check"

login_body={'j_username':'devnetuser', 
            'j_password':'Cisco123!'}

session = requests.session()
response = session.post(url, data=login_body, verify=False)

if not response.ok or response.text:
    print("Login Fail")
    import sys
    sys.exit(1)

else: 
    print("Login Success!!!")


### Get Device ###
url = "https://sandboxsdwan.cisco.com:8443/dataservice/device"

device_response = session.get(url, verify=False).json()['data']
# print(device_response)
for device in device_response:
    print(f"Hostname: {device['host-name']}")
    print(f"IP: {device['system-ip']}")
    print(f"Device ID: {device['deviceId']}")
    print(f"Model: {device['device-model']}")
    print(' ')