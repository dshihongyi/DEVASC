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

create_organization_network = CreateOrganizationNetworkModel()
params['create_organization_network'] = create_organization_network


result = networks_controller.create_organization_network(params)

