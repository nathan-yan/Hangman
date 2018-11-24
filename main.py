
stages = [
"""    
       _____
      |
      |
      |
      |
      |
-------------
""",
"""
       _____
      |     O
      |
      |
      |
      |
-------------
""",
"""
       _____
      |     O
      |     |
      |     |
      |
      |
-------------
""",
"""
       _____
      |     O
      |     |\\
      |     |
      |
      |
-------------
""",
"""
       _____
      |     O
      |    /|\\
      |     |
      |
      |
-------------
""",
"""
       _____
      |     O
      |    /|\\
      |     |
      |    /
      |
-------------
""",
"""
       _____
      |     O
      |    /|\\
      |     |
      |    / \\
      |
-------------
"""
]

import random 

def printStage(incorrect_guesses):
  print(stages[incorrect_guesses])

words = []
with open("words.txt", "r") as words_file:
  content = words_file.read()
  words = content.splitlines()

target_word = random.choice(words)
print(target_word)

number_of_guesses = 0
letters_guessed = [] # set
incorrect_guesses = 0

guess = '-' * len(target_word)
while guess != target_word:
  valid_guess = True

  # Game code hex
  while not valid_guess: 
    letter_guess = input("What letter do you guess?")

    # Go over more efficient way
    """for letter in letters_guessed:
      if letter == letter_guess:
        print("You've already guessed this letter!")

        break
    else:
      print("You haven't guessed this letter!")
      letters_guessed.append(letter_guess)
    """

    if (len(letter_guess) > 1 or letter_guess not in 'abcdefghijklmnopqrstuvwxyz'):
      valid_guess = False

    if letter_guess in letters_guessed:
      print("You've already guessed this letter!")
      valid_guess = False
    else:
      print("You haven't guessed this letter!")
      letters_guessed.append(letter_guess)


  guess_is_correct = False
  for i in range(len(target_word)):
    if (target_word[i] == letter_guess):
      guess_is_correct = True
      guess = guess[0 : i] + letter_guess + guess[i + 1 : ]

  if (not guess_is_correct):
    incorrect_guesses += 1
  
  printStage(incorrect_guesses)
  print(guess)
  print(letters_guessed)
  print("\n")
