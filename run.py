# Import random is for the rock, paper, scissors game
import random
import time


# ******* ROUND ONE ********
# ******OF CHOICE FOR USER*****


def intro():
    """
    Function intro()
    Creates input for user
    Option 1: Rope
    Option 2: Raft
    Option 3: Walk
    """
    print("$ You are now on top of Skull Island Mountain")
    time.sleep(2)
    print("$ You need to get to the base")
    time.sleep(2)
    print("$ Which option do you take?")
    time.sleep(2)
    print("""$ Option #1: Climb down the mountain face by rope,
                be careful, the rope appears old and brittle""")
    print("""$ Option #2: Make a raft and descend by Mountain River, but you don't
                know how shallow and rocky it is
                """)
    print("""$ Option #3: Walk by foot, the slowest option
                and you don't know what challenges you could face""")
    round_one = input("$ Which will you choose? (1, 2 or 3) ")

    while round_one != "1" and round_one != "2" and round_one != "3":
        round_one = input("$ Invalid Input Error: Try again ")

    if round_one == "1":
        print()
        option1()
    elif round_one == "2":
        print()
        option2()
    elif round_one == "3":
        print()
        option3()

# Round one
# option1(): if option ONE was chosen in Round 1
# Reminder continuation of: Rope


def option1():
    """
    Function option1()
    Game Over
    play again?
    yes: main()
    no : exit()
    """
    print("$ You have chosen to descend the mountain by rope")
    time.sleep(2)
    print("$ As you are half way down the rope begins to break")
    time.sleep(2)
    print("$ Oh no, the rope has snapped")
    time.sleep(2)
    print("$ You shouldn't have gone this way...")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round one
# Option2(): if option TWO was chosen in Round 1
# Reminder continuation of choosing Raft


def option2():
    """
    Function option2()
    Creates input for user
    Option 1: Left
    Option 2: Right
    """
    print("$ You are in the raft travelling downstream")
    time.sleep(2)
    print("$ Suddenly, the stream splits into two directions")
    time.sleep(2)
    print("$ Option #1: Do you go left? ")
    time.sleep(2)
    print("$ Option #2: Do you go right? ")
    time.sleep(2)
    direction = input("$ Which will you choose? (1 or 2) ")

    while direction != "1" and direction != "2":
        direction = input("$ Invalid Input Error: Try again ")

    if direction == "1":
        print()
        turn_1()
    elif direction == "2":
        print()
        turn_2()

# ****** Round TWO *******
# Left turn
# Continuation of choosing Raft in round one


def turn_1():
    """
    Function turn_1()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
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
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Below Continuation of RAFT
# Round two
# Right turn
# Continuation of choosing Raft in round one


def turn_2():
    """
    Function turn_2()
    Creates input for user
    Option 1: Down
    Option 2: Jump
    Option 3: Turn
    """
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

    while choice != "1" and choice != "2" and choice != "3":
        choice = input("$ Invalid Input Error: Try again ")

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
# Stems from Raft in round one


def down_1():
    """
    Function down_1()
    Creates input for user
    Option 1: Approach/fight
    Option 2: Stake Out
    """
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
    print("$ You realise he is asleep beside the treasure chest...")
    print("""$ Option #1: Do you approach the Oger and
         fight for the treasure? """)
    print("""$ Option #2: Do you stake out the area and wait
         for the Oger to leave?""")
    choice = input("$ Which will you choose? (1 or 2) ")

    while choice != "1" and choice != "2":
        choice = input("$ Invalid Input Error: Try again ")

    if choice == "1":
        print()
        fight_1()
    elif choice == "2":
        print()
        stakeout_2()

# **** Round Four *****
# Continuation of going down Waterfall
# Stems from Raft in round one


def fight_1():
    """
    Function fight_1()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
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
    print("The Oger runs towards you with anger on his face")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round Four
# Continuation of going down Waterfall
# Stems from Raft in round one


def stakeout_2():
    """
    Function stakeout_2()
    Guessing Game start
    """
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
    print("$ In order to open the chest you must first face two challenges")
    print("$ Let the challenges commence...")
    secret_word = "secret"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False
    print("$ Guess the riddle:")
    time.sleep(2)
    print("$ If you???ve got me, you want to share me; ")
    print("$ if you share me, you haven???t kept me.")
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
        main()
    else:
        print("You win! It's time for the next challenge...")
        rock_game()

# Round Four
# Continuation of Jump
# Stems from Raft in round one


def jump_2():
    """
    Function jump_2()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ You reach up to grab the branch")
    time.sleep(2)
    print("$ You try your best to hold on, but you begin to lose grip")
    time.sleep(2)
    print("$ Your fingers begin to slip")
    time.sleep(2)
    print("$ You can't hold on for much longer")
    time.sleep(2)
    print("$ You fall into the current and BANG you hit a rock")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round Four
# Turn the raft around
# Stems from Raft in round one


def turn_around_3():
    """
    Function turn_around_3()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ Unfortunately, the current is too strong")
    time.sleep(2)
    print("$ There is nothing you can do")
    time.sleep(2)
    print("$ You are being taken in the wrong direction")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# BELOW CONTINUATION OF WALK
# **** ROUND TWO *****
# Option3(): if option THREE was chosen in Round 1
# Reminder continuation of: Walk by foot


def option3():
    """
    Function option3()
    Creates input for user
    Option 1: Approach
    Option 2: Hide
    Option 3: Run
    """
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

    while round_two != "1" and round_two != "2" and round_two != "3":
        round_two = input("$ Invalid Input Error: Try again ")

    if round_two == "1":
        print()
        option_1()
    elif round_two == "2":
        print()
        option_2()
    elif round_two == "3":
        print()
        option_3()


# Round two
# Continuation of Approcah bush
# if option 1 chosen in round 2
# Stems from Walk in round one


def option_1():
    """
    Function option_1()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ You are very brave approcahing the bush")
    time.sleep(2)
    print("$ As you get closer, you see large paw prints in the ground")
    time.sleep(2)
    print("$ An almighty ROAR makes the ground shake")
    time.sleep(2)
    print("$ You see a Tiger jump out towards you...")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round two
# IF OPTION two WAS CHOSEN BY USER IN ROUND 2
# Hide behind the nearest tree
# Stems from Walk in round one


def option_2():
    """
    Function option_2()
    Creates input for user
    Option 1: Cave
    Option 2: Climb tree
    Option 3: Throw Rock
    """
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

    while round_three != "1" and round_three != "2" and round_three != "3":
        round_three = input("$ Invalid Input Error: Try again ")

    if round_three == "1":
        print()
        option_a()
    elif round_three == "2":
        print()
        option_b()
    elif round_three == "3":
        print()
        option_c()

# Round two
# IF OPTION THREE WAS CHOSEN BY USER IN ROUND TWO
# Reminder continutation of: Run
# Stems from Walk in round one


def option_3():
    """
    Function option_3()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ You take a deep breath")
    time.sleep(2)
    print("$ You start to make a run for it...")
    time.sleep(2)
    print("$ But, OH NO! You trip and fall to the ground..")
    time.sleep(2)
    print("$ The Tiger approaches....")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round 3
# IF OPTION TWO was chosen in Round three
# Reminder continuation of Cave
# Stems from Walk in round one

# Mini Games to unlock the treasure


def option_a():
        """
        Function: Launch first Mini Game
        """
        print("$ You have made it to the cave safely")
        time.sleep(2)
        print("$ In the distance you spot a beam of light")
        time.sleep(2)
        print("$ The treasure chest is in the cave!!!")
        time.sleep(2)
        print("$ But you must face some challenges to unlock it")
        time.sleep(2)
        print("$ Let the challenges commence...")
        print("$ There are two challenges...")
        print("$ The first challenge is GUESS the Riddle")
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
            main()
        else:
            print("")
            print("$ You win! Time for your next challenge...")
            rock_game()

# Rock, Paper, Scissors Game
# based on overstackflow code
# https://stackoverflow.com/questions/13126510/python-rock-paper-scissors-score-counter/13126598#13126598


def rock_game():
    """
    Function:
    User Selection
    Comp Selection
    Determine Winner
    First to reach score of 2
    """
    print("$ It has all come down to this, the final challenge")
    time.sleep(2)
    print("$ Instructions for Rock-Paper-Scissors : ")
    print()
    print("$ Rock crushes Scissors")
    print("$ Scissors cuts Paper")
    print("$ Paper covers Rock")
    print("$ First to make it to TWO points wins!!!")
    print("$ If you and the computer draw, no scores are given")
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

        print(f'Computer: {computer_count} - You: {user_count}')
        print()

        if user_count >= 2:
            print("YOU DID IT!!!!!")
            print("CONGRATULATIONS!!!! ")
            time.sleep(2)
            print("YOU WON TREASURE CHEST")
            print("We hope to see you soon for another adventure!")
            exit()
        elif computer_count >= 2:
            print("Oh NO! Bad luck... ")
            print("You were so close to opening the treasure...")
            print("")
            print("**** GAME ****")
            print("**** OVER ****")
            print("")
            exit()

# Round 3
# IF OPTION TWO was chosen in Round three
# Reminder continuation of Climb the tree
# Stems from Walk in round one


def option_b():
    """
    Function option_b()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ You begin to climb the tree..")
    time.sleep(2)
    print("$ You decide to sit on a big branch near the top....")
    time.sleep(2)
    print("The Tiger is at the base of the tree")
    time.sleep(2)
    print("$ Oh no!...")
    time.sleep(2)
    print("$ you feel it begin to break")
    print("$ All of a sudden the branch snaps and you fall towards the Tiger")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()

# Round four
# IF OPTION TWO was chosen in Round three
# Reminder continuation of Throw rock to distract
# Stems from Walk in round one


def option_c():
    """
    Function option_3()
    Game Over
    play again?
    yes : main()
    no : exit()
    """
    print("$ You pick up the rock")
    time.sleep(2)
    print("$ You throw it as far as you can in the opposite direction")
    time.sleep(2)
    print("$ You make a run for it")
    time.sleep(2)
    print("$ But OH NO! The Tiger spots you and chases after you")
    print("")
    print("**** GAME ****")
    print("**** OVER ****")
    print("")
    restart = input("$ Do you wish to start again? Yes/No ").lower()

    while restart != "yes" and restart != "no":
        restart = input("$ Invalid Input Error: Try again ").lower()

    if restart == "yes":
        main()
    elif restart == "no":
        print("$ See you next time!!!")
        exit()


# OPENING TEXT
# Asking user if they would like to play the game


def main():
    """ Main() execution
        Creates Input:
        yes = intro
        no = exit
    """
    print(" ")
    print(" ")
    print("     **********************")
    print("     *        ***         *")
    print("     *  Treasure Chest    *")
    print("     *  by Katie Soanes   *")
    print("     **********************")
    print(" ")
    print(" ")
    name = input("$ Enter your name ")
    print("$ Hello " + name + " welcome to TREASURE CHEST")
    time.sleep(2)
    print("$ Treasure chest is an interactive adventure game!")
    time.sleep(2)
    print("$ The game where YOU get to choose your own destiny...")
    time.sleep(1)
    print("$ To play the game you must type in your answer")
    time.sleep(1)
    print("$ followed by the enter key on your keyboard.")
    time.sleep(1)
    print("$ Before we begin, let me tell you a story...")
    time.sleep(2)
    print("$ Sometime long ago I stumbled upon a treasure map,")
    time.sleep(2)
    print("$ belonging to my great-great-grandfather...")
    time.sleep(2)
    print("$ The treasure contains gold, silver and jewels....")
    print("  worth Millions!!")
    print("$ The map leads us to Skull island which is known")
    time.sleep(2)
    print("$ to be a formidable dangerous place,")
    time.sleep(2)
    print("$ where not everyone returns...")
    time.sleep(2)
    print("So, do you have what it takes to find the treasure?")
    startGame = input("$ Yes/No: ").lower()

    while startGame != "yes" and startGame != "no":
        startGame = input("$ Invalid Input Error: Try again ").lower()

    if startGame == "no":
            main()
    elif startGame == "yes":
            intro()
main()
