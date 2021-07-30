from netmiko import ConnectHandler

with open('command_file') as f:
        command_to_send = f.read().splitlines()

with open('devices_file') as f:
        all_devices = f.read().splitlines()

for devices in all_devices:
        print('Connecting to device ' + devices)
        ip_address_of_device = devices
        ios_device = {
                'device_type': 'cisco_ios',
                'ip': 'ip_address_of_device',
                'username': 'daniel',
                'password': 'cisco',
                }
        net_connect = ConnectHandler(**ios_device)
        output = net_connect.send_config_set(command_to_send)
        print(output)