import string
import random

letter_input_1 = input("Choose a letter... "'v'" for vowels, "'c'" for consonants, "'l'" for any other character")
letter_input_2 = input("Choose a letter... "'v'" for vowels, "'c'" for consonants, "'l'" for any other character")
letter_input_3 = input("Choose a letter... "'v'" for vowels, "'c'" for consonants, "'l'" for any other character")
letter_input_4 = input("Choose a letter... "'v'" for vowels, "'c'" for consonants, "'l'" for any other character")
letter_input_5 = input("Choose a letter... "'v'" for vowels, "'c'" for consonants, "'l'" for any other character")
number_of_names = input("Please select the number of names you would like, between 1 and 50")

if number_of_names != int:
    print("Sorry, you must enter a whole number between 1 and 50")
    exit()

if int(number_of_names) > 50 or int(number_of_names) < 1:
    print("Sorry, but that number is not within the guidelines")
    exit()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letter = string.ascii_lowercase

def generator():
    if letter_input_1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input_1 == "l":
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1

    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2

    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(letter)
    else:
        letter5 = letter_input_5

    name = letter1 + letter2 + letter3 + letter4 + letter5
    return(name)

for i in range(int(number_of_names)):
    print(generator())
