# Purpose
This project was built to teach to my students at The Coder School. I also built out this project whenever I am learning a new language because it demonstrates and helps you practice many foundational programming concepts like:
- variables
- lists
- functions
- conditional statements
- loops

It also introduces you to some intermediate topics as well:
- enumerating lists
- console delay and output

# Images



# Libraries
The only library you need to install is `colorama`

`pip install colorama`

# How it works
There are two variables whose value can be changed to customize behavior of game
- `cards_per_hand` - default value is 7, determines how many cards each player starts with
- `players` - default value is 2, determines how many players in game

When the game begins the program will deal cards to all players
Then, the game will begin starting from player 1
At this point the player must choose the index of what card they want to match against card_in_play
Then the game will repeat for each player until someone has exhausted all of their cards, Uno!

# TODO
Invalid input has not been handled
- An out of range index entered by player will crash program
- Entering a non number character will crash program
