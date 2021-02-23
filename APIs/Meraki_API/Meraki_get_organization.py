import requests
import json

url = "http://dashboard.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-key': '1a2e7281463e12a81669fc04b0733c70cf9d6c69'
}

response = requests.get(url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['name'] == "DevNet Sandbox":
        orgId = response_org['id']
        print(orgId)