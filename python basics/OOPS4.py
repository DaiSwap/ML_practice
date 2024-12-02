#inheritance 
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")
        
    @staticmethod
    def stop():
        print("stop car")
        
class Toyota(Car): #inherited from the class Car
    def __init__(self,name):
        self.name = name
        
car1 = Toyota("corollis")
print(car1.name)
print(car1.start()) #no error as the toyota class is inheriting from car class
# NoTE - use parenthesis always to call the attribute
print(car1.color)