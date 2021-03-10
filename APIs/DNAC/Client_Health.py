import requests
import json


import requests

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

username = 'devnetuser'
password = 'Cisco123!'

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.post(url, headers=headers, auth=(username,password)).json()

token = response['Token']

#############################################################

urlclienthealth = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

querystring = {'timestamp':''}

payload={}
headers = {
  'x-auth-token': token,
}

response = requests.get(urlclienthealth, headers=headers, params=querystring).json()

print(json.dumps(response, indent=2, sort_keys=True))
