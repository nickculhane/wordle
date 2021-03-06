# Python Wordle clone by Nick Culhane

# import the random and colorama libraries
from colorama import init
init()
from colorama import Fore, Style
import random

def word_list():
    # generate a list of words from the txt file
    with open('5_letter_words.txt', 'r') as file:
        return file.read().splitlines()

def random_word(words):
    # return a random word from a list of words
    return random.choice(words)

def is_real_word(word, listofwords):
    # check if a word exists
    return word in listofwords
    
def check_guess(word, correct_word):
    output_string = ""
    # Print out the word with coloured letters based on the rules of Wordle.
    # keep track of letters you don't need anymore
    extra_letters = []
    # loop through all letters in guessed word
    for letter in range(len(word)):
        # it's in the right spot
        if word[letter] == correct_word[letter]:
            output_string += Fore.GREEN + word[letter]
            count_secret = correct_word.count(word[letter])
            count_guess = word.count(word[letter])
            if (count_guess == 2) and (count_secret == 1):
                extra_letters.append(word[letter])
        elif word[letter] in correct_word:
            # it is not in the word at all
            if word[letter] in extra_letters:
                output_string += Fore.RED + word[letter]
            else:
                # it is in the word, but in the wrong spot
                output_string += Fore.YELLOW + word[letter]
                count_secret = correct_word.count(word[letter])
                count_guess = word.count(word[letter])
                if (count_guess == 2) and (count_secret == 1):
                    extra_letters.append(word[letter])
        else:
            # it is not in the word
            output_string += Fore.RED + word[letter]
    return output_string

def next_guess(words):
    # Input a word, repeat until it exists
    print(Style.RESET_ALL, end="")
    user_guess = input("Please enter a guess: ").lower()
    while not is_real_word(user_guess, words):
        print(Fore.RED + "That's not a word!" + Style.RESET_ALL)
        user_guess = input("Please enter a guess: ").lower()
    return user_guess

def play(full_word_list):
    print("Python Wordle clone" + Fore.CYAN)
    
    # input the num of guesses
    num_guesses = input("How many guesses do you want? ")
    while not num_guesses.isnumeric():
        num_guesses = input("How many guesses do you want? (whole number, more than 0) ")
        if num_guesses.isnumeric():
            if int(num_guesses) <= 0:
                num_guesses = ""
    num_guesses = int(num_guesses)
    
    # chooses a word from the list
    counter = 1
    actual_word = random_word(full_word_list)
    while counter <= num_guesses:
        print(Fore.RED + f"Guess #{counter} of {num_guesses}." + Style.RESET_ALL)
        user_guess = next_guess(full_word_list)
        print(check_guess(user_guess, actual_word))
        if user_guess == actual_word:
            break
        counter += 1
    print(Style.RESET_ALL)
    if user_guess == actual_word:
        print("You won!")
    else:
        print(f"You lost!\nThe word was {actual_word}.")

# generate a list of words before you start playing
full_word_list = word_list()
play(full_word_list)
