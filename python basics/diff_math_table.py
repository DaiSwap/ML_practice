#find diff of math tables n1 & n2
n1 = int(input("one num"))
n2 = int(input("other num"))
if n1>n2:
    for i in range(1,11):
        diff = n1*i-n2*i
        print(diff,end=' ')
        i+=1
else:
    print("n1>n2")