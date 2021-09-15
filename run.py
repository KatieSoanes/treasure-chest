#Round 1
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
        round_one = input("Which will you you choose? (1, 2 or 3)")
        if round_one == "1":
                print()
                option1()
        elif round_one == "2":
                print()
                option2()
        elif round_one == "3":
                print()
                option3()


# Round 2
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




# Round 3

# Round 4

# Mini games
# Guess the riddle
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