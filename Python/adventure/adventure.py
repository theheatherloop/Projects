import time
import random


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option == response:
                return response
        print_pause("Huh!?! Can't type correctly? Let's try that again...\n")


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You're out for a run with Butters, your dog when he suddenly"
                "darts into a dark abandoned house.\n")
    print_pause("A chill runs down your spine as you reluctantly chase after"
                "him.\n")
    print_pause("As you enter the house, the door slams behind you!\n")
    print_pause("You find yourself in a dirty hallway. There's just enough"
                "light"
                "to see a door to your left and right.\n")


def right_door(items):
    print_pause("You find a group of cloaked figures gathered around what"
                "appears"
                "to be some kind of summoning circle\n")
    print_pause("They seem to be chanting something\n")
    right_room(items)


def right_room(items):
    print_pause("what would you like to do? (Enter 1, 2, or 3\n")
    r_choice = valid_input("1. Interrupt them and ask for the key\n"
                              "2. Quietly search the foot locker in the corner of"
                              "the room\n"
                              "3. Back out of the room slowly\n", ["1", "2", "3"])
    if r_choice == "1":
        interrupt(items)
    elif r_choice == "2":
        locker(items)
    elif r_choice == "3":
        leave_room(items)


def interrupt(items):
    print_pause("You reluctantly ask the group for a key..\n")
    print_pause("At that moment a scary demon appears and starts walking"
                "toward"
                "you..\n")
    print_pause("Looks like you were just in time to become a sacrifice\n")
    print_pause("You lose\n")
    play_again()


def locker(items):
    if "butters" in items:
        print_pause("You're looking through the locker...WAIT! Where'd Butters"
                    "go..??\n")
        print_pause("You look around frantically...Uh No!! He's walked into"
                    "that weird circle..\n")
        print_pause(replace_substring("The dog gets turned into a ## and bites"
                                      "your head off\n", "##", monster))
        print_pause("You lose\n")
        play_again()
    elif "key" in items:
        print_pause("There's nothing here\n")
        right_room(items)
    else:
        print_pause("You found the key!\n")
        items.append("key")
        right_room(items)


def front_door(items):
    if "key" in items:
        print_pause("The door opens!!\n")
        if "butters" in items:
            print_pause("You and Butters survived the haunted house..."
                        "for now\n")
            print_pause("You Win!\n")
            play_again()
        else:
            print_pause("You burst out the door into the street...\n")
            print_pause("Realizing you left your precious dog behind, you"
                        "start feeling guilty\n")
            print_pause("You're so engrossed in your thoughts you failed to"
                        "notice the Semi truck \n")
            print_pause("heading straight for yous blaring his horn. He slams"
                        "into you, killing you instantly\n")
            print_pause("You Lose!\n")
            play_again()
    else:
        print_pause("You try to turn the knob, but it's locked.\n")
        print_pause("Looks like you need a key to open it...\n")
        pick_door(items)


def left_door(items):
    print_pause("You open the door to you left.\n")
    print_pause("It's a bedroom\n")
    left_room(items)


def left_room(items):
    print_pause("Do you want to:\n")
    l_choice = valid_input("1. Check under the bed\n"
                           "2. Check in the closet\n"
                           "3. Leave the room\n", ["1", "2", "3"])
    if "1" in l_choice:
        under_bed(items)
    elif "2" in l_choice:
        closet(items)
    elif "3" in l_choice:
        leave_room(items)


def under_bed(items):
    if "butters" in items:
        print_pause("There's nothing here...\n")
    else:
        print_pause("You check under the bed....\n")
        print_pause("You find your Butters Whimpering in the corner!\n")
        print_pause("You quickly grab him and realize you still need to find"
                    "the key\n")
        items.append("butters")
    left_room(items)


def closet(items):
    print_pause("A bowling ball falls on your head from the top shelf..\n")
    print_pause("...killing you instantly\n")
    print_pause("You Lose!\n")
    play_again()


def leave_room(items):
    print_pause("You're back in the dark hallway\n")
    pick_door(items)


def pick_door(items):
    print_pause("What would you like to do?\n")
    choice = valid_input("1. Try the left door\n"
                         "2. Try the Right door\n"
                         "3. Try the front door\n", ["1", "2", "3"])
    if "1" == choice:
        left_door(items)
    elif "2" == choice:
        right_door(items)
    else:
        front_door(items)


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(random.choice(replacement))
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


monster = ["Ogre", "Werewolf", "Dragon", "Vampire", "Hellhound", "Cerberus"
           "Dragon Turtle", "Griffin", "Chimera", "Giant Wolpertinger"]


def play_again():
    print_pause("Would you like to play again?\n")
    replay = valid_input("1. Yes\n"
                         "2. No\n", ["1", "2"])
    if replay == "1":
        play_game()
    else:
        print("Thanks for playing!")


def play_game():
    items = []
    intro()
    pick_door(items)


play_game()
