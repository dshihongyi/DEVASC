from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113","ucspe","ucspe")
handle.login()

org = handle.query_classid(class_id="orgOrg", hierachy=True)
print(org)

servers = handle.query_classid("computeBlade")

for server in servers:
    print(server)

for server in servers:
    print(server.dn, server.num_of_cpus, server.available_memory)


blade = handle.query_dn('sys/chassis-3/blade-1')
print(blade)
handle.logout()
