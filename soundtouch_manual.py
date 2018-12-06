from libsoundtouch import soundtouch_device
from libsoundtouch.utils import Source, Type
from prettytable import PrettyTable
import re

devices = ['DEVICE_IP', # Device 1
           'DEVICE_IP', # Device 2
           'DEVICE_IP', # Device 3
           'DEVICE_IP'] # Device 4

def discoverDevices():
    x = PrettyTable()
    x.field_names = ["DEVICE NAME", "DEVICE ID", "DEVICE IP", "DEVICE MAC", "DEVICE STATUS", "ZONE STATUS", "DEVICE TYPE"]
    x.align["DEVICE NAME"] = "l"
    x.align["DEVICE ID"] = "l"
    x.align["DEVICE IP"] = "l"
    x.align["DEVICE MAC"] = "l"
    x.align["DEVICE STATUS"] = "l"
    x.align["ZONE STATUS"] = "l"
    x.align["DEVICE TYPE"] = "l"

for device in devices:
        device = soundtouch_device(device)
        status = device.status()
        zone_status = device.zone_status()
        mac = re.sub(r'(.{2})(?!$)', r'\1:', device.config.mac_address)
        
        if zone_status:
            if zone_status.is_master:
                zone_status = 'Master'
            else:
                zone_status = 'Slave'

        x.add_row([device.config.name, device.config.device_id, device.config.device_ip, mac , status.source, zone_status, device.config.type])
        
    print(x)

def findMaster():
    for device in devices:
        device = soundtouch_device(device)
        status = device.status()
        zone_status = device.zone_status()
        if zone_status:
            if zone_status.is_master:
                master = device.config.name
                print (str(master) + " is Master")

discoverDevices()
findMaster()
