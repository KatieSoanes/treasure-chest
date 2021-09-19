import random
# Import random is for the rock, paper, scissors game

# ******* ROUND ONE ******** 
# ******OF CHOICE FOR USER*****
def intro():
        print("$ You are now on top of Skull island mountain")
        print("$ You need to get to the base")
        print("$ Which option do you take?")
        print("""Option #1: Climb down the mountain face by rope,
                be careful, the rope appears old and brittle""")
        print("""Option #2: Make a raft and descend down by Mountain River, but you don't
                know how shallow and rocky it is"
                """)
        print("""Option #3: Walk by foot, the slowest option
                and you don't know what challenges you could face""")
        round_one = input("$ Which will you you choose? (1, 2 or 3)  ")
        if round_one == "1":
                print()
                option1()
        elif round_one == "2":
                print()
                option2()
        elif round_one == "3":
                print()
                option3()


# ******** ROUND TWO ******** OF CHOICE FOR USER:
# option1(): if option ONE was chosen in Round 1
# Reminder continuation of: Climb down the mountain face by rope
def option1():
    print("$ You have chosen to descend the mountain by rope")
    print("$ As you are half way down the rope begins to break")
    print("$ Oh no, the rope has snapped")
    print("$ You shouldn't have gone this way...")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again?  ").lower()
    if restart == "yes":
        main()
    else:
        print("$ See you next time!")
        exit()

# ROUND TWO
# Option2(): if option TWO was chosen in Round 1
# Reminder continuation of: Make a raft and descend down by Mountain River
def option2():
        print("You are in the raft travelling downstream")
        print("Suddenly, the stream splits into two directions")
        print("Option #1: Do you go left? ")
        print("Option #2: Do you go right? ")
        direction = input("$ Which will you you choose? (1 or 2 )")
        if direction == "1":
            print()
            turn_1()
        elif direction == "2":
            print()
            turn_2()

#Left turn
def turn_1():
        print("You decided to take the left turn")
        print("The current is getting faster and faster.....")
        print("You see a drop in the distance...")
        print("At the bottom of the drop there are...")
        print("tonnes of large sharp rocks!!!")
        print("OH NO!!!! you shouldn't have gone this way")
        print("**** GAME ****")
        print("**** OVER ****")
        print("")
        restart = input("$ Do you wish to start again?  ").lower()
        if restart == "yes":
            main()
        else:
            print("$ See you next time!")
        exit()

#Right turn
def turn_2():
        print("$ You have taken the turn to the right")
        print("$ The current begins to pick up speed")
        print("$ All of a sudden you see in the distance...")
        print("$ a Waterfall drop...")
        print("$ You also see a branch hanging over the water")
        print("$ Option #1:Take your chances and go down the Waterfall ")
        print("""Option #2: Jump to grab hold of the branch
         when you get close enough """)
        print("""$ Option #3: Try to turn your raft around and 
        go against the current""")
        choice = input("$ Which will you you choose? (1, 2 or 3 )")
        if choice == "1":
            print()
            down_1()
        elif choice == "2":
            print()
            jump_2()
        elif choice == "3":
            print()
            turn_around_3()

# ******Roud Three*******
# Conintuation of Option 2 if turn RIGHT was chosen in round 2 
#Go down Waterfall
def down_1():
    print("You are brave and decide to go down the Waterfall")
    print("As you hold on to the raft with a tight grip")
    print("The current begins to get faster and faster...")
    print("You approach the edge")
    print("BOOM!!!")
    print("You are under the water at the bottom")
    print("You swim to the surface and take a gasp for air")
    print("You swim to the land")


# Jump and grab gold of branch
def jump_2():
    print("You reach up to grab the branch")
    print("You try your best to hold on, but you begin to lose grip")
    print("Your fingers begin to slip")
    print("You can't hold on for much longer")
    print("You fall into the current and BANG you hit a rock")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again?  ").lower()
    if restart == "yes":
        main()
    else:
        print("$ See you next time!")
        exit()

# Turn the raft around
def turn_around_3():
    print("Unfortunately, the current is too strong")
    print("There is nothing you can do")
    print("You are being dragged in the wrong direction")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again?  ").lower()
    if restart == "yes":
        main()
    else:
        print("$ See you next time!")
        exit()


# ROUND TWO
# Option3(): if option THREE was chosen in Round 1
# Reminder continuation of: Walk by foot
def option3():
        print("$ You have been walking by foot for almost one hour")
        print("$ You hear a rustling in the bushes")
        print("$ What do you do next?")
        print("Option #1: Approach the bush to see what is there")
        print("Option #2: Hide behind the nearest tree")
        print("Option #3: Run as fast as you can")
        round_two = input("$ Which will you you choose? (1, 2 or 3  )")
        if round_two == "1":
                print()
                option_1()
        elif round_two == "2":
                print()
                option_2()
        elif round_two == "3":
                print()
                option_3()


# ******** ROUND THREE OF CHOICE FOR USER *********
# IF OPTION THREE WAS CHOSEN BY USER IN ROUND TWO
# (Reminder continuation of: WALK BY FOOT)
# Option 1:
# Approach the bush to see what is there
def option_1():
        print("You are very brave approcahing the bush")
        print("As you get closer, you see large paw prints in the ground")
        print("An almighty ROAR makes the ground shake")
        print("You see a Tiger jump out towards you...")
        print("")
        print("**** GAME ****")
        print("**** OVER ****")
        print("")
        restart = input("$ Do you wish to start again?  ").lower()
        if restart == "yes":
                main()
        else:
                print("$ See you next time!")
                exit()

# IF OPTION THREE WAS CHOSEN BY USER IN ROUND TWO
# (Reminder continuation of: WALK BY FOOT)
# Option 2:
# Hide behind the nearest tree
def option_2():
        print("$ As you are hiding behind the tree, the rustling sound gets louder")
        print("$ You hear a ROOOAAARRRRR")
        print("$ What do you do next?")
        print("Option #1: In the corner of your eye you spot a cave, run towards the cave")
        print("Option #2: Climb the tree")
        print("""Option #3: Throw a large rock in a different direction hoping to distract 
        the Tiger, so you can make a run for it""")
        round_three = input("$ Which will you you choose? (1, 2 or 3)  ")
        if round_three == "1":
                print()
                option_a()
        elif round_three == "2":
                print()
                option_b()
        elif round_three == "3":
                print()
                option_c()


# IF OPTION THREE WAS CHOSEN BY USER IN ROUND TWO
# (Reminder continutation of: WALK BY FOOT)
# Option 3:
# Run as fast as you can
def option_3():
        print("$ You take a deep breath")
        print("$ You start to make a run for it...")
        print("$ But, OH NO! You trip and fall to the ground..")
        print("$ The Tiger approaches....")
        print("")
        print("**** GAME ****")
        print("**** OVER ****")
        print("")
        restart = input("$ Do you wish to start again?  ").lower()
        if restart == "yes":
          main()
        else:
            print("$ See you next time!")
        exit()



# ****** Round 4 ******
# IF OPTION TWO was chosen in Round three
# Reminder continuation of HIDE BEHIND TREE
# In the corner of your eye you spot a cave
def option_a():
        print("$ You have made it to the cave safely")
        print("$ Legend has it the treasure is located in this cave")
        print("$ But you must face some challenges to unlock it")
        print("$ Let the challenges commence...") 
        print("$ The first challenge is GUESS the riddle")
        print("$ Good luck!")

# Mini games to unlock the treasure:
# Guess the riddle
# based on https://www.youtube.com/watch?v=B9ORjeQlPOA 
# Building a guessing game youtube tutorial

        secret_word = "tea"
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
        print("$ First I am dried, then I am wet.")
        print("$ The longer I swim, the more taste you get.")
        print("$ What am I?")

        while guess != secret_word and not (out_of_guesses):
            if guess_count < guess_limit:
                guess = input("Enter guess: ").lower()
                guess_count += 1
            else:
                out_of_guesses = True

        if out_of_guesses:
            print("Out of Guesses, YOU LOSE!")
        else:
            print("You win!")  
            rock_game()

# Rock, Paper, Scissors Game
# based on overstackflow code 
# https://stackoverflow.com/questions/13126510/python-rock-paper-scissors-score-counter/13126598#13126598
def rock_game():
        print("Instructions for Rock-Paper-Scissors : ")
        print()
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("First to reach THREE wins!")
computer_count = 0
user_count = 0 

while computer_count < 3 and user_count < 3:
        moves = ["rock", "paper", "rock"]
        computer_choice = random.choice(moves)
        print("(rock, paper, scissors)")
        user_choice = input("Type your choice: ").strip().lower()
        print()
        computer_wins = "The computer won this round!"
        you_win = "You won this round!"
        print(f'You played {user_choice},the computer played {computer_choice}')
        if user_choice == "scissors" and computer_choice == "rock" or \
           user_choice == "paper" and computer_choice == "scissors" or \
           user_choice == "rock" and computer_choice == "paper":
            print(computer_wins)
            computer_count += 1
        elif user_choice == "rock" and computer_choice == "scissors" or \
            user_choice == "scissors" and computer_choice == "paper" or \
                user_choice == "paper" and computer_choice == "rock":
            print(you_win)
            user_count += 1
        else:
            if user_choice == computer_choice:
                print("Its a draw!")
                computer_count += 1
                user_count += 1

        print(f'Computer: {computer_count} - You: {user_count}')
        print()

                
# Round four
# IF OPTION TWO was chosen in Round three
# Reminder continuation of HIDE BEHIND TREE
# Climb the tree
def option_b():
        print("$ You begin to climb the tree..")
        print("$ You decide to sit on a big branch near the top....")
        print("The Tiger is at the base of the tree")
        print("$ Oh no!...")
        print(" you feel it begin to break")
        print("All of a sudden the branch snaps and you fall towards the Tiger")
        print("")
        print("**** GAME ****")
        print("**** OVER ****")
        print("")
        restart = input("$ Do you wish to start again?  ").lower()
        if restart == "yes":
            main()
        else:
            print("$ See you next time!")
        exit()

# Round four
# IF OPTION TWO was chosen in Round three
# Reminder continuation of HIDE BEHIND TREE
# Throw rock to distract
def option_c(): 
        print("$ You pick up the rock")
        print("$ You throw it as far as you can in the opposite direction")
        print("You make a run for it")
        print("But OH NO! The Tiger spots you and chases after you")
        print("")
        print("**** GAME ****")
        print("**** OVER ****")
        print("")
        restart = input("$ Do you wish to start again?  ").lower()
        if restart == "yes":
            main()
        else:
            print("$ See you next time!")
        exit()


# OPENING INTRODUCTORY TEXT
# Asking user if they would like to play the game
def main():
        print(" ")
        print(" ")
        print("     **********************")
        print("     *        ***         *")
        print("     *  Treasure Chest    *")
        print("     *  by Katie Soanes   *")
        print("     **********************")
        print(" ")
        print(" ")
        name = input("Enter your name ")
        print("$ Hello " + name + " welcome to TREASURE CHEST")
        print("$ Treasure chest is an interactive adventure game!")
        print("$ The game where YOU get to choose your own destiny...")
        print("$ To play the game you must type in your answer")
        print("$ followed by the enter key on your keyboard.")
        print("$ Before we begin, let me tell you a story...")
        print("$ Sometime long ago I stumbled upon a treasure map,")
        print("$ belonging to my great-great-grandfather...")
        print("$ The treasure contains gold, silver and jewels....")
        print("worth Millions!!")
        print("$ The map leads us to Skull island which is known")
        print("$ to be a formidable dangerous place,")
        print("$ where not everyone returns...")
        print("So, do you have what it takes to find the treasure?")
        startGame = input("$ Yes/No: ").lower()
        if startGame == "no":
                main()
        elif startGame == "yes":
                intro()

main()
