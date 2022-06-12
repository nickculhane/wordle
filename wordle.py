from colorama import init
init()
from colorama import Fore, Back, Style
import random
def word_list():
    with open('5_letter_words.txt', 'r') as file:
        return file.read().splitlines()

def random_word(words):
    return words[random.randint(0, len(words) - 1)]

def is_real_word(word, listofwords):
    return word in listofwords
    
def check_guess(word, correct_word):
    output_string = ""
    extra_letters = []
    for letter in range(len(word)):
        if word[letter] == correct_word[letter]:
            output_string += Fore.GREEN + word[letter]
            count_secret = correct_word.count(word[letter])
            count_guess = word.count(word[letter])
            if (count_guess == 2) and (count_secret == 1):
                extra_letters.append(word[letter])
        elif word[letter] in correct_word:
            if word[letter] in extra_letters:
                output_string += Fore.RED + word[letter]
            else:
                output_string += Fore.YELLOW + word[letter]
                count_secret = correct_word.count(word[letter])
                count_guess = word.count(word[letter])
                if (count_guess == 2) and (count_secret == 1):
                    extra_letters.append(word[letter])
        else:
            output_string += Fore.RED + word[letter]
    return output_string

def next_guess(words):
    user_guess = Fore.MAGENTA + input("Please enter a guess: ").lower()
    while not is_real_word(user_guess, words):
        print(Fore.RED + "That's not a word!" + Style.RESET_ALL)
        user_guess = input("Please enter a guess: ").lower()
    return user_guess

def play():
    print("Python Wordle clone - created by " + Fore.GREEN + "Nick Culhane " + Fore.CYAN)
    num_guesses = input("How many guesses do you want? ")
    while not num_guesses.isnumeric():
        num_guesses = input("How many guesses do you want? (whole number, more than 0) ")
        if num_guesses.isnumeric():
            if int(num_guesses) <= 0:
                num_guesses = "a"
    num_guesses = int(num_guesses)
    full_word_list = word_list()
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
play()
