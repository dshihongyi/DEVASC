from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '1a2e7281463e12a81669fc04b0733c70cf9d6c69'
meraki = MerakiSdkClient(token)

organization_controller = meraki.organizations
network_controller = meraki.networks

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

network_result = network_controller.get_network(netId)
# pprint(network_result)



##Get speicific Network VLAN Ouput
vlans = meraki.vlans.get_network_vlans(netId)



vlan = vlans[0]
vlan['name'] = 'DSVLAN111'

updated_vlan = {}
updated_vlan['network_id'] = netId
updated_vlan['vlan_id'] = vlan['id']
updated_vlan['update_network_vlan'] = vlan

result = meraki.vlans.update_network_vlan(updated_vlan)

vlans = meraki.vlans.get_network_vlans(netId)
pprint(vlans)