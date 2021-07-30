
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


Username = input("Username:")
Password = getpass()


with open('command_file_switch') as f:
        command_list_switch = f.read().splitlines()

with open('command_file_router') as f:
        command_list_router = f.read().splitlines()

with open('command_file') as f:
        command_to_send = f.read().splitlines()

with open('devices_file') as f:
        all_devices = f.read().splitlines()


for devices in all_devices:
        print('Connecting to device ' + devices)
        ios_device = {
                'device_type':'cisco_ios', 
                'ip': devices, 
                'username': Username, 
                'password': Password
                }

        try:
                net_connect = ConnectHandler(**ios_device)

        except (AuthenticationException):
                print('Authentication Failure: ' + devices)
                continue
        except (NetMikoTimeoutException):
                print('Timeout to device ' + devices)
                continue
        except (EOFError):
                print('End of file while attemping to device ' + devices)
                continue
        except (SSHException):
                print('SSH Issue, Are you sure SSH enabled on ' + devices)
                continue
        except  unknown_error:
                print('There are some other Error ' + unknown_error)
                continue


        list_versions = ['vios_l2-ADVENTERPRISEK9-M', 'VIOS-ADVENTERPRISEK9-M']

        for software_ver in list_versions:
                print('Check for ' + software_ver)
                output_version = net_connect.send_command('show version')
                int_version = 0 # Reset intger value
                int_version = output_version.find(software_ver) # Check software version
                if int_version > 0:
                        print('Software version found: ' + software_ver)
                        break
                else:
                        print('Did not found ' + software_ver)
                

        if software_ver == 'vios_l2-ADVENTERPRISEK9-M':
                print('Running ' + software_ver + ' commands')                           
                output = net_connect.send_config_set(command_list_switch)

        elif software_ver == 'VIOS-ADVENTERPRISEK9-M':
                print('Running ' + software_ver + ' commands')
                output = net_connect.send_config_set(command_list_router)

        print(output)