#Round 1
def intro():
    print("HIII")

# Round 2

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
        print("$ to be a formidable dangerous place")
        print("$ where not everyone returns...")
        print("So, do you have whay it takes to find the treasure?")
        startGame = input(" Yes/No: ").lower()
        if startGame == "no":
                print("Oh no! Are you sure?")
                print("Last chance to play....")
                startGame = input("type yes").lower
                startGame == "yes"
                intro()
        elif startGame == "yes":
                intro()

main()