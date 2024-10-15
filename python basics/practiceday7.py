#hangman part 1 and part 2
import random
wordlist = ['template','baboon','shirts','dictate','typhoon']
display =[]
chosen_word = random.choice(wordlist)
print(chosen_word)

#chosen_word = list(chosen_word) # converting to list so can iterate over
#print(chosen_word) 
guess = input("guess the letter").lower()#converting all to lowercase


for word in chosen_word:
    
    if word == guess:
        display.append(word)
        
    else:
        display.append("_")
print(display)

  