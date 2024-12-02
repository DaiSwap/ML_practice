#polymorphism - operaator overloading
class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.img = imaginary
    def showNum(self):
        print(self.real,"i +",self.img,"j")
    #now creating a dunder funciton to add so that anyone can add complex numbers using my class
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
        
num1 = Complex(1,3)
num1.showNum()

num2 = Complex(7,8)
num2.showNum()

num3 = num1 + num2 # because of dunder function able to use the + operator and add complex numbers
num3.showNum()


        