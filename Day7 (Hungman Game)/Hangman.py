#hungman
import random
stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#create a list of words
words_list = ["baboon", "lion", "amarica", "london", "afarica", "pakistan",
              "banana", "watermalon", "mango"]


#pick an item  from the list and assign to a variable
#chosen_word
end_of_game = False
chosen_word = random.choice(words_list)
word_length = len(chosen_word)

#for testing the code
print(f'the solution is {chosen_word}')

#lives of user
lives = 6

# to print the logo
from hungman_art import  logo
print(logo)
#Create an empty list called display.
#and add as many '_' as the length of the chosen_word
display=[]
for _ in range(word_length):
    display+= "_"

#ask user for letter and store it in veriable called guess
# guess = input("Enter your letter: ").lower()
#
# #loop through each position in the chosen_word:
# #if the letter at that position matches 'guess' then
# #reveal that letter in the display at that position.
# for position in range(word_length):
#     letter =chosen_word[position]
#     print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter:{guess}")
#     if letter==guess:
#         display[position]=letter
# print(display)

#Use a while loop to let the user guess again, the loop should
#only stop once the user has guessed all the letters in the
#chosen_word and 'display has no more blanks ("_"). then you
#can tell the user they've won.

while not end_of_game:
    #ask user for letter and store it in veriable called guess
    guess = input("Guess your letter: ").lower()

    #check if user already enter the letter
    if guess in display:
        print(f"you already guess {guess}")
    #loop through each position in the chosen_word:
    #if the letter at that position matches 'guess' then
    #reveal that letter in the display at that position.
    for position in range(word_length):
        letter =chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        #Task-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(f"your remaining lifes are {lives}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #join all elements in the list and turn it into string
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game=True
        print("You win. ")
    print(stages[lives])