# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:01:38 2023

@author: tomer
"""

import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    buttn = ObjectProperty(None)
    
    
    def on_touch_down(self, touch):
        print ("Ive been clicked",touch)
        self.buttn.background_color = 0.9,0.3,0.1,1
        pass
    def on_touch_move(self, touch):
        print ("Your move",touch)
        pass
    def on_touch_up(self, touch):
        print ("Don't leave me",touch)
        self.buttn.background_color = 0.5,0.5,0.5,1
        pass

class ThirdApp(App):
    def build(self):
        return Touch()

    
if __name__ == "__main__":
    ThirdApp().run()
