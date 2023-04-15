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


class MyGrid(GridLayout):
    def __init__ (self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)
        
        self.cols = 1
        
        self.inergrid = GridLayout()
        self.inergrid.cols = 2
        
        self.inergrid.add_widget(Label(text="Name:  "))
        self.name = TextInput(multiline=False)
        self.inergrid.add_widget(self.name)
        
        self.inergrid.add_widget(Label(text="Sir Name:  "))
        self.sname = TextInput(multiline=False)
        self.inergrid.add_widget(self.sname)
        
        self.inergrid.add_widget(Label(text="e-mail:  "))
        self.email = TextInput(multiline=False)
        self.inergrid.add_widget(self.email)
        
        self.add_widget(self.inergrid)

        self.submit = Button(text="Submit", font_size=35)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
        
    def pressed(self,instance):
        fname = self.name.text
        sname = self.sname.text
        email = self.email.text
        print(fname ," " , sname , " " , email)
        self.name.text = ""
        self.sname.text =""
        self.email.text =""
        
        
class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()
    
    