import random
import string

def letter_select(character_choices,vowel_true):
    while True:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        letter = random.choice(character_choices)
        if letter in vowels == vowel_true:
            return letter

def select_characters():
    end_str = ""
    user_inp = input("type \'c\' for a consonant and \'v\' for a vowel")
    if user_inp == "v":
        end_str += letter_select(string.ascii_letters,True)
    else:
        end_str += letter_select(string.ascii_letters,False)
    # for _ in range(7):
    #     user_inp = input("type \'c\' for a consonant and \'v\' for a vowel")
    return end_str
        
print(select_characters())