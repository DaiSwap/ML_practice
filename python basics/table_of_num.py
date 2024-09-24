#given num n , print table of the num
#approach3
n = int(input())
i = 1
while i<11:
    tab = i*n
    i = 1+i 
    print(tab)# a good practice to include print before changing i condition

#my approach 1
l = [1,2,3,4,5,6,7,8,9,10]
n = int(input())
for i in l:
    l2 = n*i
    print(l2)
#approach 2
n = int(input())
for i in range(1,11):
    tab = n*i
    print(tab)  
      