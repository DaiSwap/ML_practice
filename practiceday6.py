#sum of n natural numbers
n = int(input("enter num"))
sum= 0
for i in range(1,n+1):
    sum = sum+i
    i=i+1
print(sum)    

#using while

while i<=n:
    sum = i+sum
    i +=i
print(sum)    
    
# using straigt forward method

print(n*(n+1)/2)