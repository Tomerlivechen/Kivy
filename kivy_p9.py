# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:33:49 2023

@author: tomer
"""

import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen


class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

kv=Builder.load_file("fifth.kv")






class FifthApp(App):
    def build(self):
        return kv

    
if __name__ == "__main__":
    FifthApp().run()
