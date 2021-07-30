import getpass
import telnetlib

HOST = "192.168.122.99"
user = input("Enter Your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"vlan database\n")
for n in range (2,11):
	tn.write(b"vlan " + str(n).encode('ascii') + b" name Python_VLAN_" + str(n).encode('ascii') + b"\n")
	tn.write(b"no vlan " + str(n).encode('ascii') + b"\n")
tn.write(b"exit\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
