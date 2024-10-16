import random

hangman = ["wrong1","wrong2","wrong3","wrong4","wrong5","wrong6"]
word_list = ["baboon","tomato","camels","trades"]

chosen_word = random.choice(word_list)
#print(chosen_word)
dash = ""
for letter in chosen_word:
    dash+="_"
print(dash)
correct_words = []
game_over = False
while not game_over:
    guess = input("guess a letter: ")
    display = ""
    for letter in chosen_word:
        
        if guess == letter:
            display+=guess
            correct_words.append(guess)
        elif letter in correct_words:
            display+=letter
        else:
            display+="_"
    print(display)
    if "_" not in display:
        game_over = True        
            