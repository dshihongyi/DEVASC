import requests
import json

target = "https://sbx-nxos-mgmt.cisco.com/ins"
username = "admin"
password = "Admin_1234!"

requestheaders = {"content-type" : "application/json"}
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "sh ip int brief",
    "output_format": "json",
  }
}

response = requests.post(
    target,
    data=json.dumps(payload),
    headers=requestheaders,
    auth=(username,password),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))
