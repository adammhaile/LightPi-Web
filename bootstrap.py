#Do all the setup stuff here to get it out of the main module
import sys, os

from raspledstrip.ledstrip import *
from raspledstrip.animation import *

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Check that the system is set up like we want it
dev = '/dev/spidev0.0'

if not os.path.exists(dev):
	sys.stderr.write("""
The SPI device /dev/spidev0.0 does not exist. You may need to load
the appropriate kernel modules. Try:

sudo modprobe spi_bcm2708 ; sudo modprobe spidev

You may also need to unblacklist the spi_bcm2708 module in 
/etc/modprobe.d/raspi-blacklist.conf

""")
	sys.exit(2)

#permissions check
try:
	open(dev)
except IOError as  e:
	if e.errno == 13:
		sys.stderr.write("""
It looks like SPI device /dev/spidev0.0 has the wrong permissions.
Try making it world writable:

sudo chmod a+rw /dev/spidev0.0

""")
	sys.exit(2)

import config
cfg = config.config()

num = cfg.numLEDs;
led = LEDStrip(num)
led.setChannelOrder(ChannelOrder.BRG) #Only use this if your strip does not use the GRB order
#led.setMasterBrightness(0.5) #use this to set the overall max brightness of the strip
led.all_off()