# Import random is for the rock, paper, scissors game
import random
import time


# ******* ROUND ONE ********
# ******OF CHOICE FOR USER*****
def intro():
    print("$ You are now on top of Skull island mountain")
    time.sleep(2)
    print("$ You need to get to the base")
    time.sleep(2)
    print("$ Which option do you take?")
    time.sleep(2)
    print("""$ Option #1: Climb down the mountain face by rope,
                be careful, the rope appears old and brittle""")
    print("""$ Option #2: Make a raft and descend by Mountain River, but you don't
                know how shallow and rocky it is"
                """)
    print("""$ Option #3: Walk by foot, the slowest option
                and you don't know what challenges you could face""")
    round_one = input("$ Which will you choose? (1, 2 or 3) ")
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
    time.sleep(2)
    print("$ As you are half way down the rope begins to break")
    time.sleep(2)
    print("$ Oh no, the rope has snapped")
    time.sleep(2)
    print("$ You shouldn't have gone this way...")
    time.sleep(2)
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

        print("$ You are in the raft travelling downstream")
        time.sleep(2)
        print("$ Suddenly, the stream splits into two directions")
        time.sleep(2)
        print("$ Option #1: Do you go left? ")
        print("$ Option #2: Do you go right? ")
        direction = input("$ Which will you choose? (1 or 2) ")
        if direction == "1":
            print()
            turn_1()
        elif direction == "2":
            print()
            turn_2()

# Left turn


def turn_1():

    print("$ You decided to take the left turn")
    time.sleep(2)
    print("$ The current is getting faster and faster.....")
    time.sleep(2)
    print("$ You see a drop in the distance...")
    time.sleep(2)
    print("$ At the bottom of the drop there are...")
    time.sleep(2)
    print("$ tonnes of large sharp rocks!!!")
    time.sleep(2)
    print("$ OH NO!!!! you shouldn't have gone this way")
    time.sleep(2)
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again?  ").lower()
    if restart == "yes":
        main()
    else:
        print("$ See you next time!")
        exit()

# Right turn


def turn_2():

    print("$ You have taken the turn to the right")
    time.sleep(2)
    print("$ The current begins to pick up speed")
    time.sleep(2)
    print("$ All of a sudden you see in the distance...")
    time.sleep(2)
    print("$ a Waterfall drop...")
    time.sleep(2)
    print("$ You also see a branch hanging over the water")
    time.sleep(2)
    print("$ Option #1:Take your chances and go down the Waterfall ")
    print("""Option #2: Jump to grab hold of the branch
         when you get close enough """)
    print("""$ Option #3: Try to turn your raft around and
        go against the current""")
    choice = input("$ Which will you choose? (1, 2 or 3) ")
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
# Go down Waterfall


def down_1():

    print("$ You are brave and decide to go down the Waterfall")
    time.sleep(2)
    print("$ As you hold on to the raft with a tight grip")
    time.sleep(2)
    print("$ The current begins to get faster and faster...")
    time.sleep(2)
    print("$ You approach the edge")
    time.sleep(2)
    print("$ BOOM!!!")
    time.sleep(2)
    print("$ You are under the water at the bottom")
    time.sleep(2)
    print("$ You swim to the surface and take a gasp for air")
    time.sleep(2)
    print("$ You manage to swim to the land")
    time.sleep(2)
    print("$ You see a giant Oger in the distance")
    time.sleep(2)
    print("$ You realise he is asleep beside the treasure chest")
    time.sleep(2)
    print("""$ Option #1: Do you approach the Oger and
         fight for the treasure? """)
    print("""$ Option #2: Do you stake out the area and wait
         for the Oger to leave?""")
    choice = input("$ Which will you choose? (1 or 2) ")
    if choice == "1":
        print()
        fight_1()
    elif choice == "2":
        print()
        stakeout_2()


def fight_1():

    print("As you prepare to approach the Oger")
    time.sleep(2)
    print("You take a step back and accidentally break a branch")
    time.sleep(2)
    print("The sound wakes the Oger")
    time.sleep(2)
    print("The Oger lets out a loud grunt")
    time.sleep(2)
    print("The Ogers footsteps make the ground shake")
    time.sleep(2)
    print("You are spotted")
    time.sleep(2)
    print("The Oger runs towards you with anger on his face")
    time.sleep(2)
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again?  ").lower()
    if restart == "yes":
        main()
    else:
        print("$ See you next time!")
        exit()


def stakeout_2():

    print("$ You hide behind a bush and wait for the Oger to leave")
    time.sleep(2)
    print("""$ 3 hours later you feel the ground shake as the
        Oger makes his way towards the cave in the distance
        """)
    time.sleep(2)
    print("$ Once you can no longer see the Oger in the distance")
    time.sleep(2)
    print("$ You run to the treasure chest")
    time.sleep(2)
    print("$ Congratulations, you found the treaure chest...")
    time.sleep(2)
    print("$ In order to open the chest you must first face two challenges")
    time.sleep(2)
    print("$ Let the challenges commence...")
    secret_word = "secret"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    print("$ If you’ve got me, you want to share me; ")
    print("$ if you share me, you haven’t kept me.")
    print("$ What am I?")
    print("$ HINT: I am 6 letters long")
    print("$ A _ _ _ _ _ _")
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


# Jump and grab hold of branch

def jump_2():

    print("$ You reach up to grab the branch")
    time.sleep(2)
    print("$ You try your best to hold on, but you begin to lose grip")
    time.sleep(2)
    print("$ Your fingers begin to slip")
    time.sleep(2)
    print("$ You can't hold on for much longer")
    time.sleep(2)
    print("$ You fall into the current and BANG you hit a rock")
    time.sleep(2)
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

    print("$ Unfortunately, the current is too strong")
    time.sleep(2)
    print("$ There is nothing you can do")
    time.sleep(2)
    print("$ You are being taken in the wrong direction")
    time.sleep(2)
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
    time.sleep(2)
    print("$ You hear a rustling in the bushes")
    time.sleep(2)
    print("$ What do you do next?")
    time.sleep(2)
    print("$ Option #1: Approach the bush to see what is there")
    print("$ Option #2: Hide behind the nearest tree")
    print("$ Option #3: Run as fast as you can")
    round_two = input("$ Which will you choose? (1, 2 or 3) ")
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
        print("$ You are very brave approcahing the bush")
        time.sleep(2)
        print("$ As you get closer, you see large paw prints in the ground")
        time.sleep(2)
        print("$ An almighty ROAR makes the ground shake")
        time.sleep(2)
        print("$ You see a Tiger jump out towards you...")
        time.sleep(2)
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

    print("$ As you are hiding behind the tree,")
    time.sleep(2)
    print("the rustling sound gets louder")
    time.sleep(2)
    print("$ You hear a ROOOAAARRRRR")
    time.sleep(2)
    print("$ What do you do next?")
    time.sleep(2)
    print("""$ Option #1: In the corner of your eye you spot a cave,
          you run towards the cave to take shelter""")
    print("$ Option #2: Climb the tree")
    print("""$ Option #3: Throw a large rock in a different direction hoping to distract
        the Tiger, so you can make a run for it""")
    round_three = input("$ Which will you choose? (1, 2 or 3)  ")
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
    time.sleep(2)
    print("$ You start to make a run for it...")
    time.sleep(2)
    print("$ But, OH NO! You trip and fall to the ground..")
    time.sleep(2)
    print("$ The Tiger approaches....")
    time.sleep(2)
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
        time.sleep(2)
        print("$ Legend has it the treasure is located in this cave")
        time.sleep(2)
        print("$ But you must face some challenges to unlock it")
        time.sleep(2)
        print("$ Let the challenges commence...")
        time.sleep(2)
        print("$ The first challenge is GUESS the riddle")
        time.sleep(2)
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
            print("$ Out of Guesses, YOU LOSE!")
        else:
            print("")
            print("$ You win! Time for your next challenge...")
            rock_game()

# Rock, Paper, Scissors Game
# based on overstackflow code
# https://stackoverflow.com/questions/13126510/python-rock-paper-scissors-score-counter/13126598#13126598


def rock_game():

    print("$ Instructions for Rock-Paper-Scissors : ")
    time.sleep(2)
    print()
    print("$ Rock crushes Scissors")
    time.sleep(1)
    print("$ Scissors cuts Paper")
    time.sleep(1)
    print("$ Paper covers Rock")
    time.sleep(1)
    print("$ Best out of THREE!")
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
        print(f'You played {user_choice}, Computer played {computer_choice}')
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
    # THIS CODE IS TO BE FIXED IF THERE IS A DRAW... TO KEEP PLAYING
        if user_count > computer_count:
            print("YOU DID IT!!!!!")
            print("CONGRATULATIONS!!!! YOU WON TREASURE CHEST")
            exit()
        elif computer_count > user_count:
            print("Oh NO! Bad luck... ")
            print("You were so close to opening the treasure...")
            print("")
            print("**** GAME ****")
            print("**** OVER ****")
            print("")
            exit()

# Round four
# IF OPTION TWO was chosen in Round three
# Reminder continuation of HIDE BEHIND TREE
# Climb the tree


def option_b():

    print("$ You begin to climb the tree..")
    time.sleep(2)
    print("$ You decide to sit on a big branch near the top....")
    time.sleep(2)
    print("The Tiger is at the base of the tree")
    time.sleep(2)
    print("$ Oh no!...")
    time.sleep(2)
    print("$ you feel it begin to break")
    time.sleep(2)
    print("$ All of a sudden the branch snaps and you fall towards the Tiger")
    time.sleep(2)
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
    time.sleep(2)
    print("$ You throw it as far as you can in the opposite direction")
    time.sleep(2)
    print("$ You make a run for it")
    time.sleep(2)
    print("$ But OH NO! The Tiger spots you and chases after you")
    time.sleep(2)
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
    time.sleep(1)
    name = input("Enter your name ")
    print("$ Hello " + name + " welcome to TREASURE CHEST")
    time.sleep(2)
    print("$ Treasure chest is an interactive adventure game!")
    time.sleep(2)
    print("$ The game where YOU get to choose your own destiny...")
    time.sleep(2)
    print("$ To play the game you must type in your answer")
    time.sleep(2)
    print("$ followed by the enter key on your keyboard.")
    time.sleep(2)
    print("$ Before we begin, let me tell you a story...")
    time.sleep(2)
    print("$ Sometime long ago I stumbled upon a treasure map,")
    time.sleep(2)
    print("$ belonging to my great-great-grandfather...")
    time.sleep(2)
    print("$ The treasure contains gold, silver and jewels....")
    time.sleep(2)
    print("  worth Millions!!")
    time.sleep(2)
    print("$ The map leads us to Skull island which is known")
    time.sleep(2)
    print("$ to be a formidable dangerous place,")
    time.sleep(2)
    print("$ where not everyone returns...")
    time.sleep(2)
    print("So, do you have what it takes to find the treasure?")
    startGame = input("$ Yes/No: ").lower()
    if startGame == "no":
        main()
    elif startGame == "yes":
        intro()


main()