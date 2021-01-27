from ncclient import manager
from pprint import pprint
import xml.dom.minidom
import datetime


def create_netconf_connection(username, password, host) -> manager:
    """Creates devince connection, get and converts configuration"""

    try:

        netconf_session = manager.connect(host=host, port=830, username=username,
                                          password=password,
                                          device_params={'name': 'csr'})

    except manager.operations.errors.TimeoutExpiredError:
        raise ConnectionError(f"Connection to {host} failed")
    except manager.transport.AuthenticationError:
        raise ConnectionError(f"Invalid Credentials")

    return netconf_session





def get_interfaces(username, password, host, interface_name=None) -> None:
    """Gets one interface with policies, queues, and stats"""

    if interface_name is not None:

        int_stats = f"""<filter>
                    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                    <interface>
                    <name>{interface_name}</name>
                    </interface>
                    </interfaces-state>
                    </filter>"""

        # Create NETCONF Session, get config
        netconf_session = create_netconf_connection(username, password, host)
        get_state = netconf_session.get(int_stats)
        int_info = xmltodict.parse(get_state.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]

    else:

        netconf_session = create_netconf_connection(username, password, host)
        get_state = netconf_session.get(all_ints)
        int_info = xmltodict.parse(get_state.xml)["rpc-reply"]["data"]["interfaces-state"]["interface"]

    # Check to see if value us a list or dict, makes list if not. Helps cut down on code
    make_ints_lists = is_instance(int_info)
    # Iterate through make_ints_lists using map funtion, call parses stats, send list
    list(map(parse_stats, make_ints_lists))
    main()



# router = {"host": "ios-xe-mgmt.cisco.com", 
#         "port": "10000", 
#         "username": "developer", 
#         "password": "C1sco12345"}


def main():

    print("Netconf Qos\n")
    print("1. View All Qos Interfaces")
    print("2. View Single Interface")
    print("3. Check if Interface has QoS\n")

    selection = input("Selecection: ")

    if selection == "1":
        device = input("Host: ")
        user = input("Username: ")
        pwd = input("Password: ")
        get_interfaces(username=user, password=pwd, host=device)



if __name__ == '__main__':
    main()



