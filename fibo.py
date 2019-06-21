def fibbonaci(n):
    if n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)

