import random
word_list = ["apple","template","baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for letter in chosen_word: #note - can also take len(chosen_word) and assign it to variable and use the range function
    placeholder += " _"
print(placeholder)    

correct_letters = []
game_over = False
while not game_over:
    guess = input("guess a letter- ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display = display+letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display = display+"_ "
    print(display)        
    if "_" not in display:
        game_over = True    
    

