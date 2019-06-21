class Human:

    def __init__(self,name,age, telephone):
        self.name=name
        self.age=age
        self.telephone= telephone

    def get_age(self):
        return self.age
    
    def get_telephone (self):
        return self.telephone

    def get_name(self):
        return self.name
    
    def increment_age(self):
        self.age =self.age + 1

h1= Human ('rahul', 25, 9999999)
print (h1.get_name() , "age is", h1.get_age())
print (h1.get_name() , " telephone is", h1.get_telephone())
