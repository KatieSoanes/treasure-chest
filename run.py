# ROUND ONE OF CHOICE FOR USER
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


# HERE is ROUND TWO OF CHOICE FOR USER:
# option1(): if option ONE was chosen in Round 1
# Climb down the mountain face by rope
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
# Make a raft and descend down by Mountain River
def option2():
        print("hi")

# ROUND TWO
# Option3(): if option THREE was chosen in Round 1
# Walk by foot
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



# ROUND THREE
# IF OPTION 2 was chosen by user
print("Add text here later!")

# ROUND THREE OF CHOICE 
# IF OPTION THREE WAS CHOSEN BY USER IN ROUND TWO
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

# Hide behind the nearest tree HEEERREE FIX
def option_2():
        print("$ As you are hiding behind the tree, the rustling sound gets louder")
        print("$ You hear a ROOOAAARRRRR")
        print("$ What do you do next?")
        print("Option #1: In the corner of your eye you spot a cave, run towards the cave")
        print("Option #2: Climb the tree")
        print("""Option #3: Throw a larger rock in a different direction hoping to distract 
        the Tiger, so you can make a run for it""")
        round_three = input("$ Which will you you choose? (1, 2 or 3)  ")
        if round_three == "1":
                print()
                option_a()


# Run as fast as you can
def option_3():
        print("Hey")



# Round 4

# IF OPTION TWO was chosen in Round three
# In the corner of your eye you spot a cave
def option_a():
        print("$ You have made it to the cave safely")
        print("$ Legend has it the treasure is located in this cave")
        print("$ But you must face some challenges to unlock it")
        print("$ Let the challenges commence") 
        guess_game()

# Mini games
# Guess the riddle
def guess_game():
        secret_word = "tea"
        guess = ""
        guess_count = 0
        guess_limit = 3
        out_of_guesses = False
        print("You must face the challenges")
        # ADD MORE TEXT HERE LATER ABOUT THE CHALLENGES
        print("First I am dried, then I am wet. The longer I swim, the more taste you get.")
        print("What am I?")
        print("Hint: I am three letters long")
#while guess != secret_word and not (out_of_guesses):
#if guess_count < guess_limit:
        #guess = input("Enter guess: ").lower()
        #guess_count += 1
#else:
       # out_of_guesses = True

#if out_of_guesses:
    #print("Out of Guesses, YOU LOSE!")
    #print("Go on, have another try")
    #guessing_game()
    
#else:
    #print("Well done, you got it right!")
    #print("It's time for your next challenge")


# Rock, Paper, Scissors


# OPENING INTRODUCTORY TEXT firstttt
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
        print("So, do you have whay it takes to find the treasure?")
        startGame = input("$ Yes/No: ").lower()
        if startGame == "no":
                print("$ Oh no! Are you sure?")
                print("$ Last chance to play....")
                startGame = input("$ type yes:  ").lower
                startGame == "yes"
                intro()
        elif startGame == "yes":
                intro()

main()