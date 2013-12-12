from bottle import *
import sys

from displays import *
import signal

from bootstrap import *

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
            return (200, '')
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

run(host=cfg.http_ip, port=cfg.http_port)
