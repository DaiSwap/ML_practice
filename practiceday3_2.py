# Conditional state/ logical operators& scope usage
'''
print("Welcome to Treasure Island.\n Your mission is to find the Treasure.\n You're at the crossroad.\n")
A = int(input("Do you want to go left or right? choose 0 for left and 1 for right"))
if A == 0:
    print("you have aarrived at a lake\n")
    B = input("choose whether to wait for boat or swim, choose 0 to wait,1 to swim")
    if B == 0:
        print("you reached")
    else:
        print("you died")
    
elif A == 1:
    print("you have been attacked0")
else:
    print("your journey ends here.Did not follow the instructions.")
'''
# simple if,nested if
height = int(input("tell your height in cm\n"))
bill = 0
if height>=120:
    age = int(input("how old are you?\n"))
    if age <= 12:
        bill =  10
        print("it will be 10 bucks")
    elif age <= 18:
        bill = 15
        print("it will be 15 bucks")
    else:
        bill = 20
        print("it will be 20 bucks")   
    want_photo = input("Do you want a photo? type Y or N\n")
    if want_photo == "Y":
        # add 3 bucks to theyre bill
        bill += 3 # same as bill = bill + 3
        print(f"your final bill is {bill}")
    print("Your final bill will be:",bill)            
else:
    print("not eligible")

'''
#check odd or even
A = int(input("enter any number"))
if (A%2) == 0:
    print("the number is even")
else:
    print("the number is odd")

#bmi with conditional statements
weight = float(input("enter your weight in kg\n"))
height = float(input("enter your height in metres\n"))

bmi = weight / (height ** 2)
print(round(bmi,2))
if bmi>=25:
    print("Overweight")
elif bmi>=18.5:
    print("Normal")
else:
    print("Underweight")
'''
     
        