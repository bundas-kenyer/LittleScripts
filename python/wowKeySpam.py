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
        temp_expkeys=[]
        for i in range(len(self.exceptkeys)):
            temp_expkeys.append(None)
            temp_expkeys[i]=keyboard.KeyCode().from_char(self.exceptkeys[i])
        self.exceptkeys=temp_expkeys
        self.listener=keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def not_mod(self, k):
        return (k not in [keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.alt_l, 
        keyboard.Key.shift_r, keyboard.Key.ctrl_r, keyboard.Key.alt_gr,
        keyboard.Key.space, keyboard.Key.esc, keyboard.Key.caps_lock, keyboard.Key.tab, keyboard.Key.enter])


    def on_press(self, key):
        #print(key)
        
        if self.not_mod(key) and key not in self.exceptkeys and key!=self.key_spammed and (self.count>3 or self.key_spammed==None or self.switch_running==False):
            self.count=0
            self.key_spammed=key
    
        if key==keyboard.Key.shift_l:
            if self.switch_main == False:
                self.switch_main=True
                self.switch_running=True
            else:
                if self.switch_running==True:
                    self.switch_running=False
                else:
                    self.switch_running=True
                #print("SHIFT" + str(self.switch_running))
        if key==keyboard.Key.enter:
            self.switch_main=False

    def on_release(self, key):
        pass

    #Main program related methods
    def run(self):
        self.listenerstart()
        while True:
            if self.switch_main and self.switch_running and self.key_spammed!=None:
                keyboard.Controller().tap(self.key_spammed)
                #print(self.key_spammed)
                if self.count<300:
                    self.count+=1
            
            sleep(0.01)

WowKeySpam().run()









