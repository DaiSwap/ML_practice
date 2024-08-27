#love calculator
'''
print("The Love Calculator is calculating your score...")
name1 = input("enter your name").lower()
name2 = input("enter your name").lower()
t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
e1 = name1.count("e")
t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
e2 = name2.count("e")

l1 = name1.count("l")
l2 = name2.count("l")
o1 = name1.count("o")
o2 = name2.count("o")
v1 = name1.count("v")
v2 = name2.count("v")
ee1 = name1.count("e")
ee2 = name2.count("e")
total_true = t1+t2+r1+r2+u1+u2+e1+e2
total_love = l1+l2+o1+o2+v1+v2+ee1+ee2
t1 = str(total_true)
t2 = str(total_love)
score = t1+t2
total = int(score)
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50 :
    print(f"your score is {total}, you are alright together.")
else:
    print(f"your score is {total}")
'''   
# after seeing solution -

name1 = input("enter your name")
name2 = input("enter your name")
combined_name = (name1+name2).lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_digit = t + r + u + e
#similarly for second digit
score = str(first_digit)# + second_digit
#hence finish with condiotional statements