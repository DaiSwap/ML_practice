#Create student class taking name and marks of 3 subjects as arguments in constructors.
#then create method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
            
        print(sum/3)
        
s1 = Student("pv",[24,21,22])
print("the avg marks of",s1.name,"is") 
s1.get_avg()        
               