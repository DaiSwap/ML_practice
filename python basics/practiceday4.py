import random
#import my_module
#print(my_module.my_favnumber)

# using randomization
'''
random_integer = random.randint(1,10)
random_number_0_to_1 = random.random() * 10
random_float = random.uniform(1,10)
'''

#randomly print heads or tails
random_coin = random.randint(0,1)
if random_coin == 0:
    print("heads")
else:
    print("tails")
    
    