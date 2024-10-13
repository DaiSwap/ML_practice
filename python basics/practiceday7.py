#hangman part 1
import random
wordlist = ['template','baboon','shirts','dictate','typhoon']

chosen_word = random.choice(wordlist)
print(chosen_word)
chosen_word = list(chosen_word) # converting to list so can iterate over
print(chosen_word) 
guess = input("guess a letter").lower()
 #converting all to lowercase
for word in chosen_word:
    
    if guess == word:
        print("correct")
    else:
        print("wrong")
       