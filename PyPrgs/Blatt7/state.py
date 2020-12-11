import threading, random, time

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

    def run(self):
        for i in range(1,10):
            if random.randint(0,1) == 0:
                self.state.inc(random.randint(0,100))
            else:
                self.state.sub(random.randint(0,100))


if __name__ == "__main__":
    # unsafe
    start = time.process_time_ns()
    unsafe = IntStateUnsafe()
    threads = [ChangerThread(unsafe) for i in range(1,18)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    tookUnsafe = (time.process_time_ns() - start)/1000000
    print("unsafe is %d" % unsafe.variable)
    print("computing took %.4f ms" % tookUnsafe)
    
