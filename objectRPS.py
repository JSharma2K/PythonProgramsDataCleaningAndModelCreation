# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:08:55 2019

@author: jivitesh's PC
"""
import random
class RockPaperScissor:
    def __init__(self):
        self.playerChoice=0
        self.computerChoice=0
        self.rock=1
        self.paper=2
        self.scissor=3
        
    def get_playerChoice(self):
         playerInput=int(input("please enter a number between 1 to 3 inclusive "))
         return playerInput
    
    def get_computerChoice(self):
        cC=random.randint(1,3) 
        return cC 
    
    def winner(self):
        if self.playerChoice == self.rock and self.computerChoice ==self.scissor:
            print("you chose rock",self.rock, "computer chose scissor",self.scissor)
            print("you win")
                
        elif self.playerChoice == self.rock and self.computerChoice==self.paper:
            print("you chose rock",self.rock, "computer chose paper",self.paper)
            print("you lose")
                
        elif self.playerChoice == self.paper and self.computerChoice==self.rock:
            print("you chose paper",self.paper, "computer chose rock",self.rock)
            print("you win")
            
        elif self.playerChoice == self.paper and self.computerChoice==self.scissor:
            print("you chose paper",self.paper, "computer chose scissor",self.scissor)
            print("you lose")
                
        elif self.playerChoice == self.scissor and self.computerChoice==self.paper:
            print("you chose scissor",self.scissor, "computer chose paper",self.paper)
            print("you win")
                
           
        elif self.playerChoice == self.scissor and self.computerChoice==self.rock:
            print("you chose scissor",self.scissor, "computer chose rock",self.rock)
            print("you lose")
            
        elif self.playerChoice==self.computerChoice:
            print("its a tie")
    
RPS=RockPaperScissor()
RPS.get_playerChoice()
RPS.get_computerChoice()    
RPS.winner()