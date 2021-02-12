class Device():
    
    def __init__(self, id, description, ipaddress, prefix):
        self.id = id
        self.description = description
        self.ipaddress = ipaddress
        self.prefix = prefix
 
    def show_full_name(self):
        return self.id, self.description

    @classmethod
    def device_info(self):
        print("\n" + "-" * 80)
        ide = input("Input Loopback Number: ")
        desc = input("Input Loopback Description: ")
        ip = input("Input Loopback IP Address: ")
        prefix = input("Input Loopback Subnet Mask: ")

        netconf_edit_501 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_501.xml").read()
        xml_filter_post_lpinter = netconf_edit_501.format(ide = ide, desc = desc, ip = ip, prefix = prefix)

        return xml_filter_post_lpinter

info = Device.device_info()
print(info)
# t = info.show_full_name()
# print(t)
# print(t[0])
# print(type(t[0]))
# print1
# print(Device(self.id)