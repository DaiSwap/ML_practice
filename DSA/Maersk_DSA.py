#given Dice & NUM , find sum at even positions and at odd positions given if dice is even - print even positions & if dice odd - print the numbers at odd positions.
dice = int(input("enter"))
num = input()
odd_sum = 0
even_sum = 0
for i,digit in enumerate(num):
    if (i +1) %2==0:
        even_sum+=int(digit)
    else:
        odd_sum+=int(digit)
        
if dice%2==0:
    print(even_sum)
else:
    print(odd_sum)        
    