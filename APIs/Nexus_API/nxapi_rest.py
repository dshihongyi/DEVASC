import requests
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload="{\r\n  \"aaaUser\": {\r\n    \"attributes\":{\r\n        \"name\":\"admin\",\r\n        \"pwd\":\"Admin_1234!\"\r\n    }\r\n  }\r\n}\r\n\r\n"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Cookie': 'APIC-cookie=uC+yXMCWr+5fKdhPtPGOmQHFiEcHTn/mueq1FEY8gO8nXDmCZJI7qkVhB1aTJOWHuInkapBIemDZMqIbq//c6f6xhEFpVrF+LnAa/yZnPXnps5MnOXmx2fYNhCHHl+y2x2VtD6XsZaA48UC8sOL0T9EyNtl+kOeuq2CVBot8n2c='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()
token = response ['imdata'][0]['aaaLogin']['attributes']['token']
print(token)
# pprint(response)
cookies = {}
cookies['APIC-cookie'] = token

url = "https://sbx-nxos-mgmt.cisco.com//api/node/mo/sys/intf/phys-[eth1/33].json"

payload="{\r\n\"l1PhysIf\":{\r\n\"attributes\":{\r\n\"descr\":\"Test-123\"\r\n}\r\n}\r\n}"
headers = {
   'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Content-Type': 'text/plain',
  }

put_response = requests.put(url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pprint(put_response)
