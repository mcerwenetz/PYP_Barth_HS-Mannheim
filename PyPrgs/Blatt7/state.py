import threading, random

class IntStateUnsafe:
    def __init__(self):
        self._i=0

    def inc(self,val):
        self.variable+=val

    def sub(self,val):
        self.variable-=val

    def _getI(self):
        return self._i

    def _setI(self,val):
        self._i=val

    variable = property(_getI, _setI)


class IntStateSafe:
    def __init__(self):
        self._i=0
        self.lock = threading.Lock()

    def inc(self, val):
        self.variable+=val

    def sub(self, val):
        self.variable-=val

    def _getI(self):
        with self.lock:
            return self._i

    def _setI(self,val):
        with self.lock:
            self._i=val

    variable = property(_getI, _setI)

class ChangerThread(threading.Thread):
    def __init__(self, state : IntStateSafe):
        super().__init__()
        self.state=state
        self.r = random()

    def run(self):
        for i in range(1,100001):
            self.state.inc(self.r.randint(0,100))

if __name__ == "__main__":
    unsafe = IntStateUnsafe()
    threads = [ChangerThread() for i in range(1,18)]
    for t in threads:
        t.start

    for t in threads:
        t.join()

