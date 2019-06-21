# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:24:13 2019

@author: jivitesh's PC
"""
import numpy as np
import pandas as pd

data1=[1,0.5,-7,3,9.45,5]
arr1= np.array(data1)
arr1
print(arr1.ndim)
print(np.ndim(arr1))
arr2=np.array(np.arange(1,10).reshape(3,3))
print(arr2.dtype)
arr2=arr2.astype('float64')
print(arr2.dtype)
arr3=np.array(np.arange(1,19).reshape(3,2,3))
arr2[:,0]=90
print (arr2)

df1=pd.DataFrame({"key":['a','b','b','b','e','f','g'],
"val": [1,2,3,4,5,6,7]}) 

df2=df=pd.DataFrame({"key":['a','b','b','d','f'],
"vl": [1,2,3,4,6 ]}) 

df3=pd.merge(df1,df2,how='left')
print(df3)