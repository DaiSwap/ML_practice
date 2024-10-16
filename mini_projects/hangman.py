import random

hangman = ["no more lives","1life","2lives","3lives","4lives","5lives","6lives"]
word_list = ["baboon","tomato","camels","trades"]

chosen_word = random.choice(word_list)
#print(chosen_word)
dash = ""

for letter in chosen_word:
    dash+="_"
print(dash)
#making variable life to keep track of number of chances
lives = 6
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
        print("you win")
       
    if guess not in chosen_word:
        lives = lives -1
        
        if lives ==0:
            game_over=True
            print(f"you lose, it was {chosen_word}") 
    print(hangman[lives])                
            