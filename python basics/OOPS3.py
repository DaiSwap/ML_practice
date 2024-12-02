# Static methods
class Student:
    @staticmethod
    def marks(): #self parameter is not used here , hence a staticmethod
        print(45)
s1 = Student.marks() 
