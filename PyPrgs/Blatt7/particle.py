#!/usr/bin/python3
import threading
import random
import time

class Particle:
    def __init__(self):
        self._x=0;
        self._y=0;
        self.keepMoving = True
        self.keepAlive = True
        class moveParticle:
            def __init__(self, particle):
                self._particle=particle
            def __call__(self):
                while(self._particle.keepAlive == True):
                    while(self._particle.keepMoving == True):
                        print(self._particle._y)
                        self._particle._y+=1
                        time.sleep(0.5)

                print("Thread done")
        self.moveCallable = moveParticle(self)
        self.moverThread = threading.Thread(target=self.moveCallable)
        self.moverThread.start()

    def get_position(self):
        return self._x,self._y

    def pause(self):
        self.keepMoving = False

    def cont(self):
        self.keepMoving=True
        
        


p = Particle()
time.sleep(5)
p.pause()
time.sleep(2)
p.cont()
time.sleep(2)
p.pause()
p.keepAlive=False
p.moverThread.join()
