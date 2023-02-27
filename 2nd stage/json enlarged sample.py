#json yapısını veri işleme veri kazıma için kullanacağız.
import json
import re
import time
import random

class Site:
    def __init__(self):
        self.turn=True
        self.datas=self.getdatas()

    def program(self):
        pass
    def login(self):
        pass
    def logincontrol(self):
        pass
    def loginsuccess(self):
        pass
    def loginfailure(self):
        pass


System=Site()
while System.turn:
    System.program()
        