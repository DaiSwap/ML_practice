#rock paper scissors game
import random
'''
user_input = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n"))
list = ["rock","paper","scissors"]
computer = random.randint(0,2)
print("computer chose",computer)
if computer == 0:
    if user_input ==0:
        print("tie")
    elif user_input ==1:
        print("user wins")
    elif user_input ==2:
        print("computer wins")
if computer == 1:
    if user_input ==0:
        print("comp wins")
    elif user_input ==1:
        print("tie")
    else:
        print("user wins")
if computer == 2:
    if user_input == 0:
        print("user wins")
    elif user_input == 1:
        print("comp wins")
    else:
        print("tie")
'''
#after seeing the solution
# similar - usage of lists and random.
# another question - banker roulette
names = ["angela",'ben','jenny','michael','chloe']
length = len(names)
#print(length)
paybill = random.randint(0,length-1)#length -1 very imp ,finally got the error , all test case passed
finalbill = names[paybill]
print(f"{finalbill} is going to buy meal today")
        
        
                        