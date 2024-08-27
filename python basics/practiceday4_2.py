# most common error of lists - list index out of range

letters = ["a","w","r","y","u","r"] # if index off by one
 
num_of_list = len(letters)
print(num_of_list)
print(letters[num_of_list - 1])
# hence do - print(list[num_of_list -1 ]) as letters["inside is index value"]

# nested list - list inside a list
blist = ["e","r","i","c","h"]
nested = [letters,blist]
print(nested[1])