class Investment:
    def __init__(self,principal,interest):
        self.principal=principal
        self.interest=interest
        
    def value_after(self,n):
        return (self.principal*(1+self.interest))**n
    
    def __repr__(self):
        return print("pricipal is "),str(self.principal),print("interest is "),str(self.interest)

obj=Investment(100,0.05)
print(obj.value_after(1))
print(obj)
