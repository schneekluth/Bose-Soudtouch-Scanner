from libsoundtouch import soundtouch_device, discover_devices
from libsoundtouch.utils import Source, Type
from prettytable import PrettyTable
import re

x = PrettyTable()
x.field_names = ["DEVICE NAME", "DEVICE ID", "DEVICE IP", "DEVICE MAC", "DEVICE STATUS", "ZONE STATUS", "DEVICE TYPE"]
x.align["DEVICE NAME"] = "l"
x.align["DEVICE ID"] = "l"
x.align["DEVICE IP"] = "l"
x.align["DEVICE MAC"] = "l"
x.align["DEVICE STATUS"] = "l"
x.align["ZONE STATUS"] = "l"
x.align["DEVICE TYPE"] = "l"

devices = discover_devices(timeout=2)  # Default timeout is 5 seconds

for device in devices:
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
