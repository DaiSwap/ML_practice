# using with logical operators
height = int(input("tell your height in cm\n"))
bill = 0
if height>=120:
    age = int(input("how old are you?\n"))
    if age <= 12:
        bill =  10
       
    elif age <= 18:
        bill = 15
        
    elif age >= 45 and age <= 55:
        bill = 0    
    else:
        bill = 20
        
    want_photo = input("Do you want a photo? type Y or N\n")
    if want_photo == "Y":
        # add 3 bucks to theyre bill
        bill += 3 # same as bill = bill + 3
        print(f"your final bill is {bill}")
    print("Your final bill will be:",bill)            
else:
    print("not eligible")
