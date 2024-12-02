# Abstraction , encapsulation , inheritance , polymorphism
# 1. Abstraction

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False
    def start(self):
        self.cluth = True
        self.acc = False
        self.brk = False
        print("car start")
        
c1 = car()
c1.start()

# 2. Encapsulation
# all basic codes with attributes and methods inside the class is this .

        