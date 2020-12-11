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
        limit = 100000
        for i in range(1,limit):
            if random.randint(0,1) == 0:
                self.state.inc(random.randint(0,100))
            else:
                self.state.sub(random.randint(0,100))

def test(state, kindOfTime:str):
    if kindOfTime == "p":
        start = time.process_time_ns()
    elif kindOfTime == "r":
        start = time.time()
    else:
        raise Exception("Wrong Format")
        
    threads = [ChangerThread(state) for i in range(1,18)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    took =0

    if kindOfTime == "p":
        took = (time.process_time_ns() - start)/1000000

    elif kindOfTime == "r":
        took = (time.time() - start)/1000000
    else:
        raise Exception("Wrong Format")

    return took


if __name__ == "__main__":
    state = IntStateUnsafe()
    print("unsafe")
    tookUnsafe = test(state,"p")
    print("computing took %.4f ms" % tookUnsafe)
    state = IntStateSafe()
    print("safe")
    tookSafe = test(state,"p")
    print("computing took %.4f ms" % tookSafe)
    print("safe was %f times slower than unsafe" % (tookSafe/tookUnsafe))

   
