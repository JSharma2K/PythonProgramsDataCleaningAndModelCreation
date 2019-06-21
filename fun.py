'''
num=int(input("Enter you num: "))
x=1
while x<num:
    if(num%x==0):
        print(x,"is a divisor")
    x+=1

for i in range(num):
    for x in range(num):
        print("Jivitesh ",end='')

for x in range(5):
    if x==1:
        print("AAAAAAAAAA",end='')
    elif x==2:
        print("BBBBBBB",end='')
    elif x==3:
        print("CDCDCDCD",end="")
    elif x==4:
        print("EFFFFFFG",end="")
'''
'''
for i in range(3,20,2):
    print(i,end=" ")

for i in range(10,-1,-1):
    print(i,end=" ")
'''
'''
i=0
while True:
    print('i =',i)
    i+=1
    j=0
    while True:
        print('j= ;=',j)
        j=j+1
        if(j==3):
            print("breaking inner while")
            break
    if (i==5):
        print('Breaking outre while')
        break

print("*"*6)
goal=1

if(goal==1):
    print("Goal! "*10)


string1="sexy"
print(string1[::-1])

list1=[[i,j] for i in range (2) for j in range (3)]
print (list1)

numerals={i:i*i for i in range (10)}
for key in numerals:
    print(key,"equals ",numerals[key])
'''
string1=" pyp "
print(string1.strip("p"))

print("python.cqm".strip("pcom."))

