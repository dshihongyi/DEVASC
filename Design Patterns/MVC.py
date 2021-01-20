class Device:
    ipAddress = ""
    port = ""

    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ipAddress = "192.168.1.1"
        d.port = "2001"
        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.50.1"
        d.port = "7091"
        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.100"
        d.port = "80"
        devices.append(d)

        return devices

class DevicesView:
    def showDevices(self,devices):
        for d in devices:
            print("---------")
            print("IP Address:" + d.ipAddress)
            print("Port: " + str(d.port))
            print("---------")

class DevicesController:
    def __init__(self):
        devices = Device.findDevices()

        v = DevicesView()
        v.showDevices(devices)

    def filterDevices(self, filter):
        devices = Device.filterDevices(filter)


c = DevicesController()

print("Submit", "HelloWorld")