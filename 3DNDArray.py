# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:14:39 2019

@author: jivitesh's PC
"""
import numpy as np

arr3=np.arange(5)
print(arr3) 
condition=[True,False,True]
x=[10,20,30]
y=[70,80,90]
condition=np.array(condition)
x=np.array([True,False,True,False,True])
y=np.array([False,True,False,False,True])
arr=np.where(x & y,0,np.where(x,1,np.where(y,2,3)))
print(arr)
np.loadtxt?