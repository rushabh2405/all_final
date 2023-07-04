from bluepy.btle import Peripheral, UUID, DefaultDelegate, Advertisement,Service, Characteristic, Descriptor, PeripheralError
import struct

# Define the UUID for the custom service and its characteristic
SERVICE_UUID = UUID("12345678-1234-5678-1234-56789abcdef0")
CHARACTERISTIC_UUID = UUID("12345678-1234-5678-1234-56789abcdef1")

# Define the custom service
class CustomService(Service):
    def __init__(self, uuid):
        Service.__init__(self, uuid, True)
        self.addCharacteristic(Characteristic(CHARACTERISTIC_UUID, 
                                                Characteristic.PERMISSION_READ))

# Define the BLE advertisement
class CustomAdvertisement(Advertisement):
    def __init__(self, service_uuids=[], manufacturer_data=None, 
                 service_data=None, flags=0):
        Advertisement.__init__(self)
        self.service_uuids = service_uuids
        self.manufacturer_data = manufacturer_data
        self.service_data = service_data
        self.flags = flags

    def getManufacturerData(self):
        return self.manufacturer_data

    def getServiceData(self):
        return self.service_data

    def getFlags(self):
        return self.flags

    def getServiceUUIDs(self):
        return self.service_uuids

# Define a delegate class to handle BLE events
class CustomDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("Notification received. Handle: {}, Data: {}".format(cHandle, data))

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device: {}".format(dev.addr))
        elif isNewData:
            print("Received new data from: {}".format(dev.addr))

# Set up the BLE advertisement data
adv = CustomAdvertisement(service_uuids=[SERVICE_UUID.getCommonName()], flags=0x04)

# Create the custom service and start advertising it
peripheral = Peripheral()
peripheral.setAdvertisementData(adv)
peripheral.addService(CustomService(SERVICE_UUID))
peripheral.startAdvertising()
print("Advertising started")

# Keep the script running so the advertisement continues to be broadcasted
while True:
    try:
        peripheral.waitForNotifications(1.0)
    except PeripheralError as e:
        print("Peripheral error occurred: {}".format(e))
        break

# Stop advertising and disconnect from the device
peripheral.stopAdvertising()
peripheral.disconnect()
print("Advertising stopped")
