#take string input and print chars at even indices
s = input().strip()#removes trailing whitespaces - strip()
for i in range(0,len(s),2): # important , take len(s) for str and print s[i]
    print(s[i],end="")