# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:02:04 2023

@author: tomer
"""

import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    fname=ObjectProperty(None)
    sname=ObjectProperty(None) 
    email=ObjectProperty(None)

    
    def submit(self):
        print (self.fname.text," ",self.sname.text,"",self.email.text," ")
        self.fname.text=""
        self.sname.text=""
        self.email.text=""

class MyApp(App):
    def build(self):
        return MyGrid()

    
if __name__ == "__main__":
    MyApp().run()
