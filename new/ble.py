from bluepy.btle import Scanner, DefaultDelegate, Peripheral

# Scan for BLE devices
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device:", dev.addr)

phone_addr = "D4:8A:39:8C:D7:B3" # replace with your phone's address
phone = None

while(1):
	scanner = Scanner().withDelegate(ScanDelegate())
	devices = scanner.scan(10.0)

# Find and connect to the mobile phone

	for dev in devices:
		if dev.addr == phone_addr:
			phone = Peripheral(phone_addr, 'public')
			break

	if not phone:
		print("Could not find the phone")
		# exit() 

# Send data to the phone
data_service_uuid = "1234" # replace with the UUID of the service you want to use
data_char_uuid = "5678" # replace with the UUID of the characteristic you want to use

service = phone.getServiceByUUID(data_service_uuid)
data_char = service.getCharacteristics(data_char_uuid)[0]

data = b"Hello, phone!"
data_char.write(data)

phone.disconnect()
