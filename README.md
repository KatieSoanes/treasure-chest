### Treasure Chest

### Link to live version: https://treasure-chest-game.herokuapp.com/ 


<img width="741" alt="Screenshot 2021-09-22 at 02 06 49" src="https://user-images.githubusercontent.com/84447603/134267634-ba89b0b8-7430-4f11-b292-a0f61d761eb7.png">

Treasure Chest is an interactive text-based adventure game. The aim of the game is for the user to choose their own adventure. Essentially, scenarios are described in a narrative and the user gets to input their choice out of the options given e.g. Option 1, 2, or 3. Depending on the option this leads to a new path, making the game different each time for players.

### How to Play

* User is given a scenario for example: You are on top of Skull Island Mountain and you need to get to the base. Do you 
1. Climb down the mountain face by rope
2. Make a raft and descend by Mountain River
3. Walk by foot

<img width="737" alt="Screenshot 2021-09-22 at 02 11 14" src="https://user-images.githubusercontent.com/84447603/134267952-d130ca0e-44cf-4a6f-b7cf-077f6dc09532.png">

* User then gets to input their answer, either: 1, 2 or 3.
If the user enters the incorrect input the user will be prompted with an invalid Error input message and asked to input again.

<img width="743" alt="Screenshot 2021-09-22 at 02 09 03" src="https://user-images.githubusercontent.com/84447603/134267830-7b0b6444-7ecd-4832-9445-40f7cf00b981.png">

* When the user reaches the treasure chest in order to open the treasure chest two mini-games must be played and won by the user.
1.  Guess the Riddle
* A riddle is presented, the user has three guesses to get it right. If correct moves on to the next game. If incorrect, the game is over.
2. Rock, Paper, Scissors (Reason for this game: I did not want the game to be a static game) Gets user selection, gets computer selection and a winner is determined. The first player to reach the score of 2 wins. No points are given if the user and computer draw. 

## FLOW CHART

* This is the flow chart for my game
* Colour coded:
1. Purple: Game Over
2. Orange: Raft. Remaining paths stem from Raft
3. Blue: Walk. Remaining paths stem from Walk

<img width="931" alt="FLOW CHART ONE (1)" src="https://user-images.githubusercontent.com/84447603/133942265-cb435949-b3e7-4449-b6dd-9dc319315f96.png"> 

<img width="842" alt="FLOW CHART TWO" src="https://user-images.githubusercontent.com/84447603/133942326-5646bd93-5589-4b2f-8dcc-937d19c8b11f.png">

<img width="841" alt="FLOW CHART THREE" src="https://user-images.githubusercontent.com/84447603/133942357-ef2b1364-de72-4b09-990a-c504504c4ec7.png">

### Features
* Input by user
* Input validation and error checking if user inputs incorrectly, they are prompted with an Error display. Allowing the user to input correctly
* Guess the Riddle: User has 3 chances to guess the missing word, then game is over.
* Rock, Paper, Scissors: User plays against the computer: User Selection, Computer Selection and a winner is chosen. If user and computer draw no score is given. First to reach a score of 2 wins.
* Aim of the game to make it to the end and win Treasure Chest.

### Future Features
* To add a custom print function where the user can decide if they would like a time delay or not and if so how long for.
* As game is content heavy I would like to separate logic from text in separate files.

## Imports
* Import time, to add time delay to code execution aiding the story telling narrative.
* Import random, used to randomise selection in Rock, Paper, Scissors. Allowing the user to go up against the computer, with a different response each time.


### Testing
* I have manually tested the game by ensuring each path works and the mini-games work. I have also tested in anticipation of incorrect user input that an error message appears and user must input correctly.
* I have passed the code through PEP8 Validator testing and can confirm there are no problems.
* Tested in my local terminal on git and also on Heroku terminal.
* Sent game to friends and family members asked them to purposely try and break game and also play properly.

### PEP 8 Validator

<img width="1026" alt="Screenshot 2021-09-22 at 00 08 08" src="https://user-images.githubusercontent.com/84447603/134259300-e22bc421-ad0b-40f3-a0c8-00324fbc7827.png">

### Bugs
* When I input Rock, Paper, Scissors Game there was an error as this was running before the main() function with the intro to the game. This bug has now been solved as it was an indentation error to do with the control flow of the program. Solved.
* Regarding the input error message, I initially forgot to add .lower(), this has been added now. 

### Remaining Bugs
* There are no bugs in the game

### Deployment
* Clone this repository
* Create a new Heroku app
* Added Config Var in Heroku's Settings. key: PORT and value: 8000
* Set the buildbacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy 

### Credits
*  Guess the Riddle: Building a guessing game youtube tutorial 
   https://www.youtube.com/watch?v=B9ORjeQlPOA
* Rock Paper Scissors: https://stackoverflow.com/questions/13126510/python-rock-paper-scissors-score-counter/13126598#13126598
* To find out what an adventure game is https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3 
* Heroku to deploy the app https://dashboard.heroku.com/apps
* Github: Repository hosting service


