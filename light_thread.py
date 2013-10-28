import threading
import time

class l_thread(threading.Thread):
    def __init__(self):
        super(l_thread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def _stopped(self):
        return self._stop.isSet()

class anim_thread(l_thread):
    def __init__(self, led, anim, delay = None, steps = 0):
        super(anim_thread, self).__init__()
        self._led = led
        self._anim = anim
        self._delay = delay
        self._steps = steps
        self._timeRef = 0;

    def __msTime(self):
        return time.time() * 1000.0

    def __timeElapsed(self):
        if ((__msTime()) - (self._timeRef)) > self._delay:
            self._timeRef = self.__msTime()
            return True
        else:
            return False

    def run(self):
        cur_step = 0
        while not self._stopped() and (self._steps == 0 or cur_step < self._steps):
            self._timeRef = self.__msTime();
            self._anim.step()
            self._led.update()
            cur_step += 1
            if self._delay:
                if self._stop.wait(max(0, ((self._timeRef + self._delay) - self.__msTime()) / 1000.0)):
                    break;
                
