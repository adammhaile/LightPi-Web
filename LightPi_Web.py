from bottle import *
import sys

sys.path.append("/home/pi/RPi-LPD8806")

from LPD8806 import *
from animation import *
from light_thread import *
import signal

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

num = (36*5*2);
led = LEDStrip(num)
led.setChannelOrder(ChannelOrder.BRG) #Only use this if your strip does not use the GRB order
#led.setMasterBrightness(0.5) #use this to set the overall max brightness of the strip
led.all_off()

curThread = None
lastReq = None
def logReq(req):
    global lastReq
    lastReq = req.fullpath

def endThread():
    global curThread
    if curThread:
        curThread.stop()
        curThread.join()
        curThread = None

@route('/js/<filename:path>')
def send_js(filename):
    return static_file(filename, root='js')

@route('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='css')

@route('/')
def index():
    return template('index')

@route('/api/pattern/<width:int>/<step:int>/<delay:int>/<colors:re:([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6})(-([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6}))*>')
def pattern(width, step, delay, colors):
    logReq(request)
    endThread()
    global curThread
    color_split = colors.split("-")
    color_list = [color_hex(c) for c in color_split]
    anim = ColorPattern(led, color_list, width, step)
    if delay == 0:
        delay = None
    else:
        delay = delay / 1000.0
    curThread = anim_thread(led, anim, delay)
    curThread.start()

@route('/api/fill/<color:re:([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6})>')
def fill(color):
    logReq(request)
    endThread()
    led.fill(color_hex(color))
    led.update()

@route('/api/brightness/<value:int>')
def brightness(value):
    #endThread()
    led.setMasterBrightness(value / 100.0)

@route('/api/brightness/get')
def brightness():
    return str(int(led.masterBrightness * 100))

@route('/api/off')
def off():
    endThread()
    led.all_off()

@route('/api/last')
def runLastReq():
    if lastReq and curThread is None:
        default_app().handle(lastReq)

def sigint_handler(signal, frame):
    print "Shutting down gracefully..."
    endThread()
    led.all_off()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

run(host='0.0.0.0', port=80, reloader=True)