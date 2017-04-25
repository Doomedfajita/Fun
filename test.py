import random


def make_sure_input_is_number(user_inp):
    input_len = int(len(user_inp))
    while True:
        list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(0, input_len, 1):
            character_at_position = user_inp[i]
            if (character_at_position not in list_numbers):
                return False
        return True

def check_input():
    input1 = raw_input("Input some shit: ")
    if make_sure_input_is_number(input1) == True:
        print("You're All good bro")
    else:
        print("Why you puttin in non-numbers?")


while True:
    giblets = raw_input("Wanna check? ")
    if giblets == "yes" or giblets == "Yes":
        check_input()
    else:
        print("Fine")
        break
