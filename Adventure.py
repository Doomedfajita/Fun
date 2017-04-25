import random , cmd
player_class = "not defined"
health = 100
strength = 100
mobility = 100
DESC = 'desc'
PLACE = 'place'
def starting_stats():
    global health , strength , mobility
    if player_class == "Ninja":
        health = 40
        strength = 40
        mobility = 90
        print("Health: " , health , "Strength: " , strength , "Mobility" , mobility)
    elif player_class == "Knight":
        health = 80
        strength = 90
        mobility = 50
        print("Health: " , health , "Strength: " , strength , "Mobility" , mobility)
    else:
        health = 100
        strength = 75
        mobility = 50
        print("Health: " , health , "Strength: " , strength , "Mobility" , mobility)
def check_stats():
    global health , strength , mobility
    print("Health: " , health , "Strength: " , strength , "Mobility" , mobility)


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
def class_choice():
    global player_class
    player_class_input = raw_input("Choose your class!  1. Ninja 2. Knight  3. Paladin:  ")
    while True:
        if player_class_input == "1" or player_class_input == "Ninja" or player_class_input == "Ninja":
            print ("You have chosen the Ninja class!")
            player_class = "Ninja"
            return
        elif player_class_input == "2" or player_class_input == "Knight" or player_class_input == "knight":
            print ("You have chosen the Knight class!")
            player_class = "Knight"
            return
        elif player_class_input == "3" or player_class_input == "Paladin" or player_class_input == "paladin":
            print ("You have chosen the Paladin class!")
            player_class = "Paladin"
            return
        else:
            print("Sorry I can't recognize that class type")
            player_class_input = raw_input("Choose Again!:  ")

def main_game():
    global player_class
    raw_input('Welcome to your adventure!  Press enter to continue ')
    class_choice()
    condition1 = True
    while condition1 == True:
        raw_input ("..........")
        raw_input ("..........")
        raw_input ("You wake up covered in dirt with a raging headache.  Everything is blurry")
        raw_input ("'Where am I?' you ask yourself.")
        raw_input ("As your vision clears, you find yourself next to a wide, dirt road")
        decision1 = raw_input("Do you 1. Get up and adventure down the unknown road 2. Stay where you are and go to sleep:   ")
        if decision1 == "1" or decision1 == "one":
            condition1 = False
        elif decision1 == "2" or decision1 == "two":
            print("You drift back into slumber")
        else:
            print("Bro just pick one of the options - stop trying to break stuff")
    raw_input ("You strectch your legs and realize that you feel a little dizzy.  You should check your stats!  Type in help to see all commands ")
def help(self):
    print ("Your available option(s) are: check_stats")

world_rooms = {
    'Main Street': {
        DESC:  "The street is bustling with people",
        PLACE: ["Baker"]},
}

interpreter = MyCmdInterpreter()
interpreter.cmdloop()
main_game()
