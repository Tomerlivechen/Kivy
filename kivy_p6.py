# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:34:48 2023

@author: tomer
"""

import kivy

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class SecondApp(App):
    def build(self):
        return FloatLayout()

    
if __name__ == "__main__":
    SecondApp().run()
