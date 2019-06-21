# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:42:24 2019

@author: jivitesh's PC
"""


class investment:
    def __init__(self,principal,interest):
        self.principal=principal
        self.interest=interest
        
    def value_after(self,years):
        value= self.principal*((1+self.interest)**years)
        print (value)
    
obj1=investment(100,0.05)
obj1.value_after(5)

dir(str())

class time:
    def __init__(self,seconds):
        self.seconds=seconds 
        
    def convert_to_minutes(self):
        minutes=(self.seconds)//60
        secs=self.seconds%60
        return minutes,":",secs
    def convert_to_hours(self):
        hours=self.seconds//3600
        seconds_left=(self.seconds % 3600)
        minutes=seconds_left//60
        remaining_seconds=seconds_left%60
        print( hours,minutes,remaining_seconds,sep=':')

obj2=time(3700)
obj2.convert_to_minutes()
obj2.convert_to_hours()