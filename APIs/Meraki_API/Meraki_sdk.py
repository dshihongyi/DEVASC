from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '1a2e7281463e12a81669fc04b0733c70cf9d6c69'
meraki = MerakiSdkClient(token)
orgs = meraki.organizations.get_organizations()

for org in orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

params = {}
params['organization_id'] = orgId
networks = meraki.networks.get_organization_networks(params) 
# pprint(networks)


for network in networks:
    if network['name'] == 'Site 2':
        netId = network['id']
    
vlan = meraki.vlans.get_network_vlans(netId)
pprint(vlan)

