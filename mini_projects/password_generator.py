# multiple comments use - ctrl +/
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to basic pyPassword generator")
in_letters = int(input("How many letters would u like in your password?"))
in_symbols = int(input("How many symbols would you like ?"))
in_numbers = int(input("How many numbers would you like?"))

password = ""

for letter in range(1,in_letters+1):
    password += random.choice(letters)
for number in range(1,in_numbers+1):
    password += random.choice(numbers)
for symbol in range(1,in_symbols+1):
    password += random.choice(symbols)

strong_pass = list(password)
print(password)

# print(strong_pass)

# new_pass = ""
# for letter in strong_pass:
#     new_pass += random.choice(strong_pass)   # here repetition of char is happening
# print(new_pass)  


#using random.shuffle()
random.shuffle(strong_pass)
password = ""
for i in strong_pass:
    password+=i
print(password)    
    

