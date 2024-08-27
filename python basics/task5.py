# print out random list of friends names
import random
rand_list = ["aditya","mia","palash","suraj","harsh","soup","ankit","samarth"]
print(random.choice(rand_list))#option1

#option2 - better one interms of understanding
random_index = random.randint(0,6)
print(rand_list[random_index])