print("Welcome to python pizza")
pizza_type = input("Choose which type of pizza you want? 'small' or 'medium' or 'large'\n")
bill = 0
if pizza_type == "small":
    
    bill = 15
    toppins = input("do you want pepporoni? Y or N")
    if toppins == "Y":
        bill += 2
        
elif pizza_type == "medium":
    
    bill = 20
    toppins = input("do you want pepporoni? Y or N\n")
    if toppins == "Y":
        bill += 3
elif pizza_type == "large":
    
    bill = 25   
    toppins = input("do you want pepporoni? Y or N\n")
    if toppins == "Y":
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N\n")
if extra_cheese =="Y":
    bill += 1

print(f"your total bill is {bill}")          