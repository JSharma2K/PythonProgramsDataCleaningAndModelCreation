# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:07:07 2019

@author: jivitesh's PC
"""
class Node:
    def __init__(self,data=None,pointer=None):
        self.data=data
        self.pointer=pointer

class SimpleLinkedList:
    def __init__(self):
        self.top=None 

    def printList(self):
        print('current state of the list')
        current=self.top
        while current!=None:
            print(current.data,end='-->')
            current=current.next
        print('None') 
    
    def addnode(self,data):
        node=Node(data)
        node.next=self.top
        self.top=node
    
    def removenode(self):
        currentPoint=self.top
        while self.top.next!=None:
            previousPointer=currentPoint
            self.top=self.top.next
            previousPointer.next=Nones
        print (self.top.data)
        print('removing bottom node', self.top.data)
        
list1=SimpleLinkedList()
list1.printList()
list1.addnode(10)
list1.printList()
list1.addnode(20)
list1.printList()
list1.addnode(30)
list1.printList()
list1.removenode()
