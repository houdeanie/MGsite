from pyHS100 import Discover
from pyHS100 import SmartPlug
from pprint import pformat as pf


def discover_device():
    for dev in Discover.discover().values():
        print(dev)

def get_device_info():
    print("Hardware: %s" % pf(plug.hw_info))
    print("Full sysinfo: %s" % pf(plug.get_sysinfo())) # this prints lots of information about the device
    

def get_device_power():
    plug = SmartPlug("192.168.43.204")
    print("Current state: %s" % plug.state)
    print("Current consumption: %s" % plug.get_emeter_realtime())

# plug.turn_off()
# plug.turn_on()
#plug.state = "ON"
#plug.state = "OFF"

