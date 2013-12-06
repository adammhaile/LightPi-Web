from LPD8806 import *
from animation import *
from light_thread import *
import inspect

class off_thread(BaseAnimation):
    """Keep the lights off."""

    def __init__(self, led, start=0, end=0):
        super(off_thread, self).__init__(led, start, end)

    def step(self, amt=1):
        self._led.all_off()

def get_delay(delay):
    if delay == 0:
        return None
    else:
        return delay

def all_off(led, params):
    led.all_off()
    return (None, '')

def all_off_thread(led, params):
    anim = [{'anim' : off_thread(led), 'delay' : 60 * 5 * 1000, 'steps' : 0, 'amt' : 1}]
    return (anim_thread(led, anim), '')

def fill_color(led, params):
    if 'color' in params:
        led.fill(color_hex(params['color']))
        led.update()
    return (None, '')

def handlePixPercent(led, val):
    result = 0;
    if type(val) is str or type(val) is unicode:
        if val.endswith("%"):
            i = float(val.rstrip('%'))
            result = int(led.leds * (i / 100.0))
        elif val.endswith("px"):
            i = int(val.rstrip("px"))
            result = i
    else:
        result = val
    return result

def handleBatchParams(led, params):
    if params:
        if 'width' in params:
            params['width'] = handlePixPercent(led, params['width'])
        if 'colors' in params:
            params['colors'] = [color_hex(c) for c in params['colors']]
    return params

#Class Utils
def getRequiredArgs(theClass):
    args, varargs, varkw, defaults = inspect.getargspec(theClass.__init__)
    if defaults:
        args = args[:-len(defaults)]
    return args   # *args and **kwargs are not required, so ignore them.

def missingArgs(theClass, argdict):
    return set(getRequiredArgs(theClass)).difference(argdict).difference(set(['self','led']))
    
def invalidArgs(theClass, argdict):
    args, varargs, varkw, defaults = inspect.getargspec(theClass.__init__)
    if varkw: return set()  # All accepted
    return set(argdict) - set(args)
#end Class Utils

batch_options = {}

def buildAnimClasses():
    for c in BaseAnimation.__subclasses__():
        batch_options[c.__name__] = c

def genBatchDict(led, item):
    if item['anim'] in batch_options:
        anim = batch_options[item['anim']]
        params = handleBatchParams(led, item['params'])
        missing = missingArgs(anim, params)
        invalid = invalidArgs(anim, params)
        error = ''
        if len(missing) > 0:
            error += (item['anim'] + ' is missing these required arguments: ' + ', '.join(missing) + '\n')
        if len(invalid) > 0:
            error += (item['anim'] + ' has some invalid arguments: ' + ', '.join(invalid) + '\n')
        if len(error) > 0:
            return (None, error)
        return ({'anim' : batch_options[item['anim']](led, **params), 'delay' : item['delay'], 'steps' : item['max'], 'amt' : handlePixPercent(led, item['amt'])}, '')
    else:
        return (None, item['anim'] + ' is not a valid animation class!\n')

def batch_anim(led, params):
    result = []
    errors = ''
    for a in params:
        dict, error = genBatchDict(led, a)
        if dict:
            result.append(dict)
        else:
            errors += error
    if len(errors) > 0:
        return (None, errors)
    return (anim_thread(led, result), '')


display_options = {
    'off_' : all_off,
    'off' : all_off_thread,
    'fill_color' : fill_color,
    'batch' : batch_anim,
}
