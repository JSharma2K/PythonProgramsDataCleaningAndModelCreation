name=input("enetr your word ")
letter=input("enetr your letter ")
i=0
p=False
while i<len(name):
    if name[i]==letter:
        print("found at index", i)
        p=True
    i+=1
if i==len(name)and p==False:
    print("not found")

