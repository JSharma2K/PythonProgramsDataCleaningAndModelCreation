# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:02:47 2019

@author: jivitesh's PC
"""
import numpy as np
alphabets=np.array(['A','B','C','A','C'])
print(alphabets)
data=np.random.randn(5,4)
print(data)
print(alphabets=='A' )
print(data[alphabets=='A'])
