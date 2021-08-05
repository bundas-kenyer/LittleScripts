#required libs: pynput, time

from pynput import keyboard
from time import sleep

class WowKeySpam():
    key_spammed=None
    key_wanted=None
    count=0
    exceptkeys="wasdcvmploykj"

    switch_main=True
    switch_running=False

    flag_run=False
    flag_listener=False

    listener=None


    #Listener related methods
    def listenerstart(self):
        self.listener=keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            if key.char not in self.exceptkeys and key.char!=self.key_spammed and (self.count>3 or self.key_spammed==None or self.switch_running==False):
                self.count=0
                self.key_spammed=key.char
        except:
            if key==keyboard.Key.shift_l:
                if self.switch_running==True:
                    self.switch_running=False
                else:
                    self.switch_running=True
                print("SHIFT" + str(self.switch_running))
    def on_release(self, key):
        try:
            pass
        except:
            pass

    #Main program related methods
    def run(self):
        self.listenerstart()
        while True:
            if self.switch_main and self.switch_running and self.key_spammed!=None:
                keyboard.Controller().tap(self.key_spammed)
                if self.count<300:
                    self.count+=1
            
            sleep(0.01)

WowKeySpam().run()













