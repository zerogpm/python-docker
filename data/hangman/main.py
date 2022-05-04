import random
import hangman_art
from word_list import word_list
#Step 1

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
print(hangman_art.logo)
count_word_choose = len(chosen_word)
for letter in chosen_word:
    display.append("_")

end_of_the_game = False
player_life = 6

while not end_of_the_game:
    guess = input("Guess your letter ")
    guessed = guess.lower()
    for position in range(count_word_choose):
        letter = chosen_word[position]
        if letter == guessed:
            display[position] = letter

    if "_" not in display:
        end_of_the_game = True
        print("You win")

    print(display)

    if guess not in chosen_word:
        print(f"you guessed {guess}, that is not in the word, you lose a life.")
        player_life -= 1
        if player_life == 0:
            print("you lose")
            print(f"the choose word is {chosen_word}")
            end_of_the_game = True

    print(hangman_art.stages[player_life])

    if guess in chosen_word:
        print(f"you guess {guess} before")
