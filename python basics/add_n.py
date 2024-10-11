# gauss calc of 1 till 100 - he figured out there are 50 pairs of 101 additions hence - 50*101 = 5050
# using for loop with range
print(range(1,10)) # notice it doesnt print 1 till 10.Can only be used with other function like for
sum = 0
for i in range(1,101): #raneg is always n,n-1
    sum += i
print(sum)    