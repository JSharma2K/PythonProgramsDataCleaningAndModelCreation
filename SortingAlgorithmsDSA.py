# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:57:47 2019

@author: jivitesh's PC
"""

#seraching algorithms discussed linear serach- O(n),Binary search-O(log n), interpolation search-O(log of log n)
#while nalaysing sorting agorithms parameters to see if algorthm is good
#1. no of comparisons
#2.recursively or iteratively implemented
#3.Space complexity
#4. no.0f swaps 
#5.number of inversions or unnecessary swaps
#types of sorting logos
#1 internal/external
#2 comparsion based

#Bubble Sort (comparsion based sorting algo)
"""
def swap(a,b):
    temp=b
    b=a
    a=temp
    return a,b

def BubbleSort(Array):
    for i in range(len(Array)):
        for j in range(len(Array)-1):
            if Array[j]>Array[j+1]:
                temp=Array[j+1]
                Array[j+1]=Array[j]
                Array[j]=temp
    print (Array)
    

def bubbleSort2(A):
	comparisons = 0
	n = len(A)
	for i in range(n):
		for j in range(n-1, i, -1):
			comparisons += 1
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
	print comparisons
	return A

def bubbleSort(A):
	swappingNeeded = False
	n = len(A)
	for i in range(n-1):
		if A[i] > A[i+1]:
			swappingNeeded = True
			break
	if swappingNeeded == False:
		return A
	for i in range(n):
		for j in range(n-1, i, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
	return A
	
A = [3,60,2,40,16,19, -9, 4, 8, 0]
print bubbleSort(A)
A= [-9, 0, 2, 3, 4, 8, 16, 19, 40, 60]
print bubbleSort(A)


BubbleSort(A)
""" 
#selection sort
"""
def selection_sort(array):
    for i in range(len(array)):
        minElement=i
        for j in range(i+1,len(array)):
            if array[minElement]> array[j]:
                minElement=j
            if i != minElement:
                array[i],array[minElement]=array[minElement],array[i]
    return array
    
A=[3,5,2]
print(selection_sort(A) )   
"""
# tree sort for hw inorder traversal on a balanced binary search tree
"""
def insertion_Sort(Array):
    for i in range(1,n):
        curr=A[i]
        index=i
        while(index>0 and curr<Array[index-1]:
            Array[index]=Array[index-1]
            index-=1
            Array[index]=curr
    return Array
"""

def mergeSort(A):
 if len(A)==1:
     return A
 else:
     mid=len(A)//2
     leftSubArray=A[:mid]
     rightSubArray=A[mid:]
     mergeSort(leftSubArray)
     mergeSort(rightSubArray)
     i=j=k=0
     while(i<len(leftSubArray) and j<len(rightSubArray)):
         if leftSubArray[i]< rightSubArray[j]:
             A[k]=leftSubArray[i]
             i+=1
         else:
             A[k]=rightSubArray[j]
             j+=1
         k+=1
     while(i<len(leftSubArray)):
         A[k]=leftSubArray[i]
         i+=1
         k+=1
     while(i<len(leftSubArray)):
         A[k]=rightSubArray[j]
         j+=1
         k+=1
         return A
         
   

A=[6,1,10,3,16,28,19,20,1]

print(mergeSort(A))

        
    