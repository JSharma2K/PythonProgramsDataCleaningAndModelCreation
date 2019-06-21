'''
s=input("enter a formula")
openBrackets=0
closeBracket=0
diff=0
listVersion=list(s)
for characterFront in range(len(listVersion)):
    if listVersion[characterFront]=="(":
        openBrackets+=1   
    for characterBack in range(-1,len(listVersion),-1):
        if listVersion[chracterBack]==")":
             closeBracket+=1
if openBrackets==closeBracket:
    print("open :",openBrackets,"close :",closeBracket,"equal number so formula is well formed")
'''
'''
formula=input("enter a formula :")
stack=[]
balanced= True
for character in formula:
    if character=="(":
        stach.append(character)
    elif character==")":
        if len(stack)==0:
            balanced=False
            break
        else:
            stack.pop(len(stack)-1)
if balanced and (len(stack)==0):
    print("formula is good")
else:
    print("formula is wrong")

'''
'''
for x in range(0,5):
    print("*")
    for x in range(0,10):
        print("*",end='')
'''
def Divide_list(l,n):
    list2=[x/n for x in l]
    return list2

def Multiply(l,n):
    list3=[x*n for x in l]
    return list3





def getMean(l):
    sum=0
    for x in l:
        sum+=x
    return sum/len(l)
list1={}
def main():
    list1=[i*2 for i in range(1,10)]
    list2=[x*2 for x in list1 if x>=25]
    print(list1)
    print(list2)
   #print(getMean(list1))
   #print(getMean(list2))
    Divide_list(list1,2)

if __name__=="__main__":
    main()
    
def obscure(x):
    if x in "aeiou":
        return "."
    elif x==" ":
        return "/"
    else:
        return"_"
s= "python rulz"
print("".join(list(map(obscure,s))))

        
    
    
            
        
