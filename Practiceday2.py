'''
#Tipcalculator
print("let us find out how much tip you owe!")
A = input("what was the total bill\n")
print("How much tip would you like to give?")

# subscripting
print("Hello"[0])
print("Hello"[-1])
print(123_345_456) #LArge integer,  _ just for reading puerpose , makes no changes
print(56.8765) #Float data type & Floating point number 

#Boolean values 
print(True)
print(False)

print(type(False))#to return the type of dataset
print(len("hello"))# return only length of string and not int/float

#type conversion
print(int("123")+int("34")) #str to int using int()

#ERROR - print("Number of letters in your name:\n" + len(input("enter your name\n")))

A = len(input("Enter your name\n"))
print("Number of letters in your name is:" + str(A)) # Did type conversion here

# math op basic- PEMDASLR/BODMAS
print(5/10)
print(type(5/10))# implicit type casting
print(5//10)
print(2**2)# ** - exponent
'''
#f-strings - print(f""")
score = 2
height = 5.3
is_winning = False

print(f"Your score is = {score} and your height is {height} . You win might be {is_winning}")