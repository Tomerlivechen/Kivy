# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:17:56 2023

@author: tomer
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:01:38 2023

@author: tomer
"""

import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.properties import ObjectProperty

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        
        with self.canvas:
            Color(1,0,0,0.3, mode="rgba")
            self.rect = Rectangle(pos=(0,0),size=(50,50))
    
    def on_touch_down(self, touch):
        self.rect.pos=touch.pos
        print ("Ive been clicked",touch)
        pass
    def on_touch_move(self, touch):
        self.rect.pos=touch.pos
        print ("Your move",touch)
        pass


class FourthdApp(App):
    def build(self):
        return Touch()

    
if __name__ == "__main__":
    FourthdApp().run()
