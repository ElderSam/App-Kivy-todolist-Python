# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:39:23 2020

@author: samuel
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Tech With Tim")
    
    
if __name__ == "__main__":
    MyApp().run()
