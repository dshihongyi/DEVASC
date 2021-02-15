

class Edit_Filters():     # String Option - Configure Data - Filter Template
    
    # def __init__(self, ide, description, ipaddress, prefix):
    #     self.ide = ide
    #     self.description = description
    #     self.ipaddress = ipaddress
    #     self.prefix = prefix

    def post_lpinter(self):    # String Option 501 - Create Loopback Interface
        netconf_edit_501 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_501.xml").read()
        xml_filter_post_lpinter = netconf_edit_501.format(ide = self.ide, desc = self.desc, ip = self.ip, prefix = self.prefix)
        edit_request(xml_filter_post_lpinter)
    
    def del_lpinter(self):     # String Option 502 - Delete Loopback Interface
        netconf_edit_502 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_delete_502.xml").read()
        xml_filter_del_lpinter = netconf_edit_502.format(ide = self.ide)
        edit_request(xml_filter_del_lpinter)

    def put_lpinter(self):     # String Option 503 - Edit Loopback Interface
        netconf_edit_503 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_503.xml").read()
        xml_filter_put_lpinter = netconf_edit_503.format(ide = self.ide, desc = self.desc, ip = self.ip, prefix = self.prefix)
        edit_request(xml_filter_put_lpinter)

    def put_gbinter(self):     # String Option 504 - Edit Gigabit Interface
        netconf_edit_504 = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_edit_504.xml").read()
        xml_filter_put_gpinter = netconf_edit_504.format(ide = self.ide, desc = self.desc)
        edit_request(xml_filter_put_gpinter)


class Show_Filters():     # String Option - Fetch Data - Filter Template

    def get_run(self):
        xml_filter_running = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_0.xml").read()
        get_request(xml_filter_running)
    
    def get_inter(self):
        xml_filter_inter   = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_101.xml").read()
        get_request(xml_filter_inter)
    
    def get_gbinter(self):
        xml_filter_gbinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_102.xml").read()
        get_request(xml_filter_gbinter)

    def get_lpinter(self):
        xml_filter_lpinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_103.xml").read()
        get_request(xml_filter_lpinter)   

    def get_ipinter(self):
        xml_filter_ipinter = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_104.xml").read()
        get_request(xml_filter_ipinter) 

    def get_route_all(self):
        xml_filter_router  = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_201.xml").read()
        get_request(xml_filter_router)

    def get_host(self):
        xml_filter_host    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_301.xml").read()
        get_request(xml_filter_host) 

    def get_user(self):
        xml_filter_user    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_302.xml").read()
        get_request(xml_filter_user) 

    def get_license(self):
        xml_filter_lic     = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_303.xml").read()
        get_request(xml_filter_lic)

    def get_line(self):
        xml_filter_mgmt    = open("e:/Github/DEVASC/NETCONF/NETCONF_GET_EDIT/Filter_Template/netconf_get_304.xml").read()
        get_request(xml_filter_mgmt)
