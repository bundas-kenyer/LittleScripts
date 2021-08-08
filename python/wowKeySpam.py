#required libs: pynput, time

from pynput import keyboard
from time import sleep

class WowKeySpam():
    key_spammed=None
    key_mod_spammed=None
    count=0

    exceptkeys= set([keyboard.KeyCode.from_char(c) for c in "wasdcvmploykj"])
    validkeys=(set([keyboard.KeyCode.from_char(chr(c)) for c in range(ord('0'),ord('9')+1)]+
        [keyboard.KeyCode.from_char(chr(c)) for c in range(ord('a'),ord('z')+1) if keyboard.KeyCode.from_char(chr(c))]))

    switch_main=True
    switch_running=False

    listener=None

    #Listener related methods
    def listenerstart(self):
        self.listener=keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def not_mod(self, k):
        return (k not in [keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.alt_l, 
        keyboard.Key.shift_r, keyboard.Key.ctrl_r, keyboard.Key.alt_gr,
        keyboard.Key.space, keyboard.Key.esc, keyboard.Key.caps_lock, keyboard.Key.tab, keyboard.Key.enter])

    def on_press(self, key):
        if (self.not_mod(key) and key not in self.exceptkeys and key in self.validkeys and key!=self.key_spammed and
            (self.count>3 or self.key_spammed==None or self.switch_running==False)):
            self.count=0
            self.key_spammed=key
            self.key_mod_spammed=None
        elif key==keyboard.Key.shift_l:
            if self.switch_main == False:
                self.switch_main=True
                self.switch_running=True
            else:
                if self.switch_running==True:
                    self.switch_running=False
                    self.key_mod_spammed=None
                else:
                    self.switch_running=True
        elif key==keyboard.Key.enter:
            self.switch_main=False
        elif key in [keyboard.Key.ctrl_l, keyboard.Key.alt_l] and self.key_mod_spammed not in [keyboard.Key.ctrl_l, keyboard.Key.alt_l]:
            self.key_mod_spammed=key

    def on_release(self, key):
        pass

    #Main program related methods
    def run(self):
        self.listenerstart()
        while True:
            kms=self.key_mod_spammed
            if self.switch_main and self.switch_running and self.key_spammed!=None:
                if kms!=None:
                    keyboard.Controller().press(kms)
                    keyboard.Controller().press(self.key_spammed)
                    keyboard.Controller().release(self.key_spammed)
                    keyboard.Controller().release(kms)
                else:
                    keyboard.Controller().tap(self.key_spammed)
                if self.count<300:
                    self.count+=1
            sleep(0.01)

WowKeySpam().run()
