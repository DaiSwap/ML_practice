#given num n , print table of the num
#approach3 , incase user asked specefic num of multiples
n = int(input())
m = int(input("num of multiples: "))
i = 1
while i<=m:
    tab = i*n
    i = 1+i 
    print(tab)# a good practice to include print before changing i condition

#my approach 1
l = int(input("num of multiples: "))
n = int(input())
for i in l:
    l2 = n*i #error - object is not iterable because l is a int and it is not iterable like list or range
    print(l2)
#approach 2
n = int(input())
l = int(input("enter num of multiples"))
for i in range(1,l+1):
    tab = n*i
    print(tab)  
      