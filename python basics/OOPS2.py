#methods

class Student:
    def __init__(self,name):
        self.name = name
        
    def start(self):   #method , this is the function 
        print("hello",self.name) 
        
s1 = Student("pv")
s1.start()    