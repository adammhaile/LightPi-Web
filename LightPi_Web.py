from bottle import *
import sys

sys.path.append("/home/pi/RPi-LPD8806")

from LPD8806 import *
from animation import *
from light_thread import *

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

num = 36*5*2;
led = LEDStrip(num)
led.setChannelOrder(ChannelOrder.BRG) #Only use this if your strip does not use the GRB order
#led.setMasterBrightness(0.5) #use this to set the overall max brightness of the strip
led.all_off()

curThread = None
def endThread():
    global curThread
    if curThread:
        curThread.stop()
        curThread.join()
        curThread = None

@route('/')
def index():
    return template('index')

@route('/api/pattern/<index:int>')
def pattern(index):
    endThread()
    global curThread
    if index == 0:
        anim = ColorPattern(led, [Color(255,0,0),Color(0,255,0)],2)
        curThread = anim_thread(led, anim)
        curThread.start()

@route('/api/on')
def on():
    endThread()
    led.fill(SysColors.red)
    led.update()
    return "LEDs on!"

@route('/api/off')
def off():
    endThread()
    led.all_off()
    return "LEDs off!"

@route('/api/<action>/<value>')
def main_api(action, value):
    return template('You chose action: {{action}} with value: {{value}}', action=action, value=value)

run(host='0.0.0.0', port=80)