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
    def __init__(self, led, anims):
        super(anim_thread, self).__init__()
        self._led = led
        self._anims = anims
        self._timeRef = 0;
        self._curAnim = 0;

        print "anim_thread"
        print anims

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
        current = self._anims[self._curAnim]
        anim = current["anim"]
        delay = current["delay"]
        max_steps = current["steps"]
        amount = current["amt"]
        while not self._stopped():
            self._timeRef = self.__msTime();
            anim.step(amount)
            self._led.update()

            if delay:
                #false return means that the thread was already stopped, so break
                if self._stop.wait(max(0, ((self._timeRef + delay) - self.__msTime()) / 1000.0)):
                    break;

            #if multiple anims, move to next one
            if len(self._anims) > 1:
                cur_step += 1
                if cur_step >= max_steps:
                    cur_step = 0
                    self._curAnim += 1
                    if self._curAnim >= len(self._anims):
                        self._curAnim = 0
                    self._led.fillOff() #switch everythign off between animations
                    current = self._anims[self._curAnim]
                    anim = current["anim"]
                    delay = current["delay"]
                    max_steps = current["steps"]
                    amount = current["amt"]
                
