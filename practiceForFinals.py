from random import *
for i in range(0,5):
    print('*'*i)

for i in range(3,0,-1):
    print('*'*i)

def factorial(n):
    if type(n) is int and n>0:
        fact=1
        for i in range(n,1,-1):
            fact=fact*i
        return(fact)
    else:
        print("wrong input")

#print(factorial(-5))

s=''
for i in range(10):
    t=input("enter a letter")
    if t in 'aeiou':
        s=s+t
        print(s)
    
str1='HELLO'

def stringFunction(str1='HELLO'):
    print(len(str1))
    print(str1*10)
    print(str1[0])
    print(str1[:3])
    print(str1[::-1])
    
def pallindrome(n):
    if n==n[::-1]:
        return True
    else:
        return False
print(pallindrome('pop'))
print(pallindrome('kill'))



list1=[0 for i in range(13)]
for i in range(10001):
    dice=randint(1,6)+ randint(1,6)
    list1[dice]=list1[dice]+1

"""        
for i in range(len(list1)):
                 print(list1[i]/10000)
    
help(dict.values())
"""
stringFunction()
