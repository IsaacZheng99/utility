"""
an easy custom implementation of Timer
"""
from typing import Dict
import time
import threading


class Timer(threading.Thread):
    def __init__(self, sThreadName):
        super(Timer, self).__init__(name=sThreadName)
        self.m_Funcs: Dict = {}
        self.m_MinInterval: int = 1  # the minimum interval is 1 second
    
    def add_func(self, oFunc, sFlag: str, iStartTime: int, iInterval: int, *args):
        if sFlag not in self.m_Funcs:
            self.m_Funcs[sFlag] = [oFunc, iStartTime, iInterval, *args]
    
    def run(self):
        while True:
            time.sleep(self.m_MinInterval)
            iCurTime: int = int(time.time())
            for oFunc, iStartTime, iInterval, *args in self.m_Funcs.values():
                if iStartTime <= iCurTime and not (iCurTime - iStartTime) % iInterval:
                    oFunc(*args)

def test(iValue: int):
    print(iValue)

oTimer = Timer('MyTimer')
oTimer.start()
oTimer.add_func(test, 'test', int(time.time()), 1, 123)
