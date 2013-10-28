from bottle import *
import sys

sys.path.append("/home/pi/RPi-LPD8806")

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
    curThread = display_options["off"](led, None)
    if curThread:
        curThread.start()

def doParamsHandling(params):
    global led
    if params:
        if 'width' in params:
            w = params['width']
            if type(w) is str or type(w) is unicode:
                if w.endswith("%"):
                    wi = int(w.rstrip('%'))
                    params['width'] = int(led.leds * (wi / 100.0))
                elif w.endswith("px"):
                    wi = int(w.rstrip("px"))
                    params['width'] = wi
    return params

def __handleJSON(json_data):
    global curThread
    print json_data
    if 'display' in json_data:
        if json_data['display'] in display_options and 'params' in json_data:
            endThread()
            params = doParamsHandling(json_data['params'])
            curThread = display_options[json_data['display']](led, params)
            if curThread:
                curThread.start()
            return "OK"
        else:
            return "FAIL"
    else:
        return "FAIL"

@post('/api/json')
def json():
    return __handleJSON(request.json)

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

run(host='0.0.0.0', port=80)
