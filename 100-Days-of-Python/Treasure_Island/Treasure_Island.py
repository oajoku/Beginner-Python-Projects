print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choose_direction =input("You're at a crossroad, where would you like to go? Left or Right? ").lower()


if choose_direction == "left":
    pick_route = input('You\'ve come to a lake.'
                       ' There is an Island in the middle of the lake. '
                       'Type "Swim" to swim across.'
                       ' Type "Wait" to wait for a boat?\n ').lower() #Continue in the game.
    if pick_route == "wait":
        which_door = input("You've arrived at a house unharmed."
                           " There is a house with three doors. "
                           "One red, one yellow, one blue."
                           " Which colour do you choose? "
                           "Red, Yellow or Blue?\n ").lower()
        if which_door == "yellow":
            print("Amazing, You found the treasure! "
                  "You Win!")
            players_reward = input("For your reward, pick between a Car and a Puppy!\n").lower()
            if players_reward == "Car":
                print("Amazing, Here's your brand new Car!")
            else:
                print("Great, Here's your brand new Puppy!")
        elif which_door == "Red":
             print("You've entered a burning house."
                   "You've been burned by fire! "
                   "Game Over! ")
        elif which_door == "Blue":
             print("You've entered a room full of snakes. "
                   "You've been eaten by Snakes! "
                   "You lose, Game Over!")
        else:
            print("You chose a door that doesn't exist."
                  "Game Over!")
    else:
        print("You've been attacked by a six sharks, Game Over!")

elif choose_direction == "Right":
    wrong_route = "You Lose, Game Over!"
    print(wrong_route)
else:
    wrong_route = "You Lose, Game Over!"
    print(wrong_route)

