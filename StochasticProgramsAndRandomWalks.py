# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:11:56 2019

@author: jivitesh's PC
"""
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
class coin:
    def __init__(self):
        self.heads=0
        self.tails=0
        self.count=0
    def coinToss(self,numTosses):
        while self.count<numTosses:
            Toss=random.randint(0,1)
            if Toss==1:
                self.heads+=1
            else:
                    self.tails+=1 
            self.count+=1
            
    def Count(self):
        ProbHeads=self.heads/self.count
        ProbTails=self.tails/self.count 
        print(ProbHeads,":heads",ProbTails,":tails")
        
Coin=coin()
Coin=coin()
Coin.coinToss(100000) 
Coin.Count()   
"""
  
def NumTimes(Tosses):
    list1=[random.randint(0,1) for x in range(Tosses)]
    print((list1.count(1)/len(list1))/(list1.count(0)/len(list1))

df=pd.DataFrame(
 {"10":[NumTimes(10)],
  "100":[NumTimes(100)],
  "1000":[NumTimes(1000)]})

print(df)


