def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
def binom(n,k):
    first=fact(n)
    second= fact(k)*fact(n-k)
    return first/second
    

print(binom(5,3))



