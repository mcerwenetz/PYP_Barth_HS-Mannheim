import threading

threading.Barr

class IntState:
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

if __name__ == "__main__":
    pass
