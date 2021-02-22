import requests
import json
import re

switch_username = 'admin'
switch_passowrd = "Admin_1234!"
url = "https://sbx-nxos-mgmt.cisco.com/ins"
header = {'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
}

response = requests.post(url, data=json.dumps(payload), headers=header, auth=(switch_username,switch_passowrd), verify=False).json()

############### LOGIN WITH NX-API RESST ###################

auth_url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"
auth_body = {"aaaUser": {"attributes" : {"name" : "admin", "pwd" : "Admin_1234!"}}}

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Cookie': 'APIC-cookie=uC+yXMCWr+5fKdhPtPGOmQHFiEcHTn/mueq1FEY8gO8nXDmCZJI7qkVhB1aTJOWHuInkapBIemDZMqIbq//c6f6xhEFpVrF+LnAa/yZnPXnps5MnOXmx2fYNhCHHl+y2x2VtD6XsZaA48UC8sOL0T9EyNtl+kOeuq2CVBot8n2c='
}

auth_response = requests.post(auth_url, data=json.dumps(auth_body), headers=headers,
timeout=5, verify=False).json()

token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies={}
cookies['APIC-token']=token


################ MANIPULATE THE DATA #################

counter=0
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']
print(nei_count)

while counter < nei_count:
  hostname   = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
  local_int  = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
  remote_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']

  payload={"l1PhysIf":{"attributes":{"descr":'Connect to' + hostname + 'Remote interface is ' + remote_int}}}

  counter += 1

  if local_int != 'mgmt0':
      int_name = str.lower(str(local_int[:3]))
      int_num = re.search(r'[1-9]/[1-9]*', local_int)
      int_url = 'https://sbx-nxos-mgmt.cisco.com//api/node/mo/sys/intf/phys-['+int_name+ str(int_num.group(0))+'].json'
      post_response= requests.post(int_url, data=json.dumps(payload), headers=headers, cookies=cookies, verify=False).json()
      print(post_response)