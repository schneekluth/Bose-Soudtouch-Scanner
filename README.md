# Bose-Soudtouch-Scanner
List all Bose Soundtouch devices on your network incl. zone status.

![Screenshot](https://raw.githubusercontent.com/schneekluth/Bose-Soudtouch-Scanner/master/preview.jpg)

### Prerequisites
pip3 install libsoundtouch PTable

### How to use
You'll find two files in this repo:  

1.`soundtouch_autodiscovery.py`: just type `python soudntouch_autodiscovery.py` into your terminal and you'll see the list in the screenshot above. Devices are automatically discovered via mdns.  
2.`soundtouch_manual.py`: If your devices have static IPs enter them in this file (Replace DEVICE_IP with real IP). This works faster that the autodiscovery. There are two functions: One to draw the table and one to find the current master if devices are zoning.
