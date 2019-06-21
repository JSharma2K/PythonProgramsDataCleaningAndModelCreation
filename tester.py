binary=int(input("enter your binary string: "))
power=0
decimal=0
while binary>0:
    decimal+=2**power*(binary%10)
    binary//=10
    power+=1
print("decimal: " ,decimal)
    
    
