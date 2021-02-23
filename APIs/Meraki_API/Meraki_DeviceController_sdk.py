from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '1a2e7281463e12a81669fc04b0733c70cf9d6c69'
meraki = MerakiSdkClient(token)

organization_controller = meraki.organizations
network_controller = meraki.networks
device_controller = meraki.devices

##Get Organization
orgs = organization_controller.get_organizations()

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']
params = {}
params['organization_id'] = orgId
networks = network_controller.get_organization_networks(params) 
# pprint(networks)

##Get speicific Network ID Ouput
for network in networks:
    if network['name'] == 'DevNet Sandbox ALWAYS ON':
        netId = network['id']

device_result = device_controller.get_network_devices(netId)

for item in device_result:
    print('Device Model: ' + item.get('model'))

for i in device_result:
    print('Device Model is ' + i['model'])



