import requests
import json
from pprint import pprint

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload={
    "aaaUser":{
        "attributes": {
            "name": "admin",
            "pwd":"ciscopsdt"
        }
    }
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()

token = response ['imdata'][0]['aaaLogin']['attributes']['token']
# print(token)
cookie = {}
cookie["APIC-cookie"] = token


url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json"

headers = {
  'x-auth-token': 'dGoAAAAAAAAAAAAAAAAAANAh/aURjbOXMT574fuVfra07LUPkad/z+CtNqli3/It9EwgS0bdBtueRlrweNTo3pxuRlE4gbKInhd/4T+tSGZfIsIeZUREGRwrINp+0c0A3Q2MGTykJz5tPqlB56GWoJkRAHET4iYz+zR6yfxjUqzBf7pr9ZGmNnaPhOerdP08R2AfrDLGAIMG0EFdi3DkCQ=='
}

get_response = requests.get(url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))


########### UPDATE APN DESCRIPTION ###########

post_payload =  {
    "fvAp": {
        "attributes": {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}

post_response = requests.post(
    url, headers=headers, cookies=cookie, data=json.dumps(post_payload), verify=False).json()

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))