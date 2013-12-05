from LPD8806 import *
from animation import *
from light_thread import *

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
    return None

def all_off_thread(led, params):
    anim = [{'anim' : off_thread(led), 'delay' : 60 * 5 * 1000, 'steps' : 0, 'amt' : 1}]
    return anim_thread(led, anim)

def fill_color(led, params):
    if 'color' in params:
        led.fill(color_hex(params['color']))
        led.update()
    return None

def pattern(led, params):
    if 'width' in params and 'step' in params and 'colors' in params and 'delay' in params:
        color_list = [color_hex(c) for c in params['colors']]
        anim = ColorPattern(led, color_list, params['width'], params['step'])
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def larson(led, params):
    if 'tail' in params and 'color' in params and 'delay' in params:
        anim = LarsonScanner(led, color_hex(params['color']), params['tail'])
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def larson_rainbow(led, params):
    if 'tail' in params and 'delay' in params:
        anim = LarsonRainbow(led, params['tail'])
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def rainbow_cycle(led, params):
    if 'delay' in params:
        anim = RainbowCycle(led)
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def color_wipe(led, params):
    if 'delay' in params and 'color' in params:
        anim = ColorWipe(led, color_hex(params['color']))
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def color_chase(led, params):
    if 'delay' in params and 'color' in params:
        anim = ColorChase(led, color_hex(params['color']))
        return anim_thread(led, anim, get_delay(params['delay']))
    return None

def rainbow(led, params):
    if 'delay' in params:
        anim = [{'anim' : Rainbow(led), 'delay' : 0, 'steps' : 0, 'amt' : 1}]
        return anim_thread(led, anim)
    return None

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

def getPattern(led, params):
    params = handleBatchParams(led, params)
    return ColorPattern(led, params['colors'], params['width'], params['dir'], params['start'], params['end'])

batch_options = {
    "pattern" : getPattern,
}

def genBatchDict(led, item):
    if item['anim'] in batch_options:
        return {'anim' : batch_options[item['anim']](led, item['params']), 'delay' : item['delay'], 'steps' : item['max'], 'amt' : handlePixPercent(led, item['amt'])}
    else:
        return None

def batch_anim(led, params):
    result = []
    for a in params:
        result.append(genBatchDict(led, a))
    return anim_thread(led, result)


display_options = {
    'off_' : all_off,
    'off' : all_off_thread,
    'fill_color' : fill_color,
    'pattern' : pattern,
    'larson' : larson,
    'larson_rainbow' : larson_rainbow,
    'rainbow' : rainbow,
    'rainbow_cycle' : rainbow_cycle,
    'color_wipe' : color_wipe,
    'color_chase' : color_chase,
    'batch' : batch_anim,
}
