from LPD8806 import *
from animation import *
from light_thread import *

def get_delay(delay):
    if delay == 0:
        return None
    else:
        return delay

def all_off(led, params):
    led.all_off()
    return None

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

def rainbow(led, params):
    if 'delay' in params:
        anim = Rainbow(led)
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


display_options = {
    'off' : all_off,
    'fill_color' : fill_color,
    'pattern' : pattern,
    'larson' : larson,
    'larson_rainbow' : larson_rainbow,
    'rainbow' : rainbow,
    'rainbow_cycle' : rainbow_cycle,
    'color_wipe' : color_wipe,
    'color_chase' : color_chase,
}
