# Reeborg world maze -
# link - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# my solution - wont pass all cases -
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def walk():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()  
        
while not at_goal():
    walk()

# solution - brute forcing right path following

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def walk():
    
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()  
        
while not at_goal():
    walk()

# above solution got stuck in an infinite loop of a square.
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def walk():
    
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()  

while front_is_clear():
    move()
turn_left()    
while not at_goal():
    walk()

#still very bad code , not optimized and takes lot of steps.    
    
    


        
        

    