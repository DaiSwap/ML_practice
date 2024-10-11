#functions - defining our function
def my_function(): # function with parenthesis and then colon
    print("learn1") #do this
    print("learn2") # then do this , always indented
    
my_function() #calling functions

#reborg solving - link - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def walk():
    move()
    jump()


for step in range(0,6):
    walk()
    

    

