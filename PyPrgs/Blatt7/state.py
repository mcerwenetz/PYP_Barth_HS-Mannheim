import threading, random
from abc import ABC, abstractmethod

class IntState(ABC):

    @abstractmethod 
    def inc(self,val):
        pass

    @abstractmethod 
    def sub(self,val):
        pass


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


    # def inc(self, val):
        # self.variable+=val

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
    def __init__(self, state):
        super().__init__()
        self.state=state
        self.random = random()

    def run(self):
        # for i in range(1,100001):
        pass

if __name__ == "__main__":
    intS= IntStateSafe()
