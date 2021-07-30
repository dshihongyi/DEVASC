import getpass
import telnetlib

user = input("Enter Your Username: ")
password = getpass.getpass()

f = open("myswitches")


for IP in f:
        IP = IP.strip()
        print("Configuring Switches " + IP)
        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")

        if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"config t\n")
        tn.write(b"no ip domain lookup\n")
        tn.write(b"exit\n")
        tn.write(b"term len 0\n")
        tn.write(b"sh run \n")
        tn.write(b"exit")

        readoutput = tn.read_all()
        saveoutput = open("switch" + HOST, "w+")
        saveoutput.write(readoutput.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close



import getpass
import telnetlib
import time

user = input("Enter Your Username: ")
password = getpass.getpass()

f = open("myswitches")


for IP in f:
        IP = IP.strip()
        print("Configuring Switches " + IP)
        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")

        if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"sh run \n")
        time.sleep(5)

        readoutput = tn.read_all()
        saveoutput = open("switch" + HOST, "w+")
        saveoutput.write(readoutput.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close




import getpass
import telnetlib
import time

user = input("Enter Your Username: ")
password = getpass.getpass()

f = open("myswitches")


for IP in f:
        IP = IP.strip()
        print("Configuring Switches " + IP)
        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        
        if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write("terminal length 0\n")
        tn.write("show version\n")
        tn.wirte("exit\n")
        print tn.read_all()
