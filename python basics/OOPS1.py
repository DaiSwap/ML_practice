# #created class
# class Car:
#     color = "blue"
#     brand = "BE"
# #created object(instances)    
# car1 = Car()
# print(car1.color) 
# print(car1.brand)   

#Constructors - init fucntion
class Student:
    college_name = "ruas" #class attribute
    def __init__(self, name, marks):
        self.name = name   #instance attributes
        self.marks = marks
        print("Add new stud to database")
        
s1 = Student("pv",45)    
print(s1.name)    
print(s1.marks)
s2 = Student("mia",55)

print(s2.name, s2.marks) # the output will be - First constructor called for the s1 then again for s2.

print(s1.college_name, Student.college_name) #calling class attribute