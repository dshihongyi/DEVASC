import json
from napalm import get_network_driver

devicelist = ['192.168.122.91', '192.168.122.100']


for ip_address in devicelist:
	print("Connecting to " + str(ip_address))
	driver = get_network_driver('ios')
	iosv = driver(ip_address, 'daniel', 'cisco')
	iosv.open()
	iosv.load_merge_candidate(filename='ACL1.cfg')
	diffs = iosv.compare_config()
	if len(diffs) > 0:
        	print(diffs)
        	iosv.commit_config()
	else:
    		print("No Change Required")

	iosv.load_merge_candidate(filename='ospf1.cfg')

	diffs = iosv.compare_config()
	if len(diffs) > 0:
        	print(diffs)
        	iosv.commit_config()
	else:
        	print("No Change Required")

	iosv.close()