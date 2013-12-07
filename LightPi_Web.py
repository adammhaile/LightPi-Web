from bottle import *
import sys

sys.path.append("/home/pi/RPi-LPD8806")

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from displays import *
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
    global led
    led.fill(SysColors.off)
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

@route('/<filename:path>')
def send_css(filename):
    return static_file(filename, root='')

import traceback
def __doOffThread():
    global curThread
    endThread()
    curThread, error = display_options["off"](led, None)
    if curThread:
        curThread.start()

def __handleJSON(json_data):
    global curThread
    print json_data
    if 'display' in json_data:
        if json_data['display'] in display_options and 'params' in json_data:
            endThread()
            params = json_data['params']
            curThread, error = display_options[json_data['display']](led, params)
            if len(error):
                return (501, error)
            if curThread:
                curThread.start()
            return (200, "OK")
        else:
            return (501, json_data['display'] + ' is not a valid display object!')
    else:
        return (501, 'JSON requests require a display parameter')

@post('/api/json')
def json():
    status, msg = __handleJSON(request.json)
    response.status = status
    if len(msg) > 0:
        print msg
    return msg

@route('/')
def index():
    #return template('index')
    return static_file("index.html", root='')

@route('/api/off')
def off():
    endThread()
    led.all_off()

def sigint_handler(signal, frame):
    print "Shutting down gracefully..."
    endThread()
    led.all_off()
    sys.exit(0)

__doOffThread()

signal.signal(signal.SIGINT, sigint_handler)

if len(batch_options) == 0:
    buildAnimClasses()

run(host='0.0.0.0', port=80)
