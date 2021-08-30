from colorama import Fore
from os import system, name
import time, random


def print_card_in_color(card):
    """
    recieves a card as parameter
    check the first character of the card for its color
    then print the card according to its color
    """
    if card == "Draw":
        print(Fore.WHITE + "Draw")
    elif card[0] == "R":
        print(Fore.RED + card)
    elif card[0] == "Y":
        print(Fore.YELLOW + card)
    elif card[0] == "G":
        print(Fore.GREEN + card)
    elif card[0] == "B":
        print(Fore.BLUE + card)


def print_hand(hand):
    """
    print every card in the hand
    call print_card_in_color on each card
    """
    for i, card in enumerate(hand):
        print(Fore.WHITE + "[" + str(i) + "] - ", end="")
        print_card_in_color(card)
    print()


def play_card(position, hand):
    """
    according to position selected by user:
      - draw a card, return
      - remove card from hand
    """

    card = hand[position]
    if card == "Draw":
        new_card = cards.pop()
        hand.append(new_card)
        return card_in_play
    del hand[position]
    return card


def validate_card(card_in_play, hand, card_choice_index):
    """
    validate that the user selected card matches card_in_play

    if the player makes an incorrect choice they must try again
    """
    card_choice = hand[card_choice_index]

    if card_choice == "Draw":
        return True
    elif card_in_play[0] == card_choice[0]:  # color
        return True
    elif card_in_play[1] == card_choice[1]:  # number
        return True
    else:  # invalid card
        return False


def clear():
    """
    clear console output so next player cant see prev player cards
    """
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


cards = [
    "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
    "Y0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9",
    "G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"
]
random.shuffle(cards)
random.shuffle(cards)

"""
The value of these 2 variables can be changed to directly affect the behavior of game
"""
cards_per_hand = 7
num_of_players = 2

"""
deal cards to each player
"""
hands = []
for i in range(num_of_players):
    hand = [cards.pop() for j in range(cards_per_hand)]
    hand.insert(0, "Draw")
    hands.append(hand)

# the card each player must match
card_in_play = cards.pop()

# when the player runs out of cards then running will become False
running = True
while running:

    # loop through the hands (each players hand)
    for i, hand in enumerate(hands):

        # before taking input, print out their hand
        print(Fore.WHITE + "Current card in play: ", end="")
        print_card_in_color(card_in_play)
        print_hand(hand)
        card_choice_index = int(input(Fore.WHITE + "Player " + str(i + 1) + ", enter what card you want to play: "))

        # if the player enters an invalid card ask them to try again until valid
        while not validate_card(card_in_play, hand, card_choice_index):
            print("Incorrect choice")
            card_choice_index = int(input(Fore.WHITE + "Player " + str(i + 1) + ", enter what card you want to play: "))

        # change the value of card_in_play to the card the user chose
        card_in_play = play_card(card_choice_index, hand)

        # if a hand has only 1 card left (the Draw card) then they have won, end the game
        if len(hand) == 1:
            running = False
            print("Player " + str(i + 1) + " wins!")
            print("Ending Game...")
            break

        # print the players hand again so they can see what they have after completing their turn
        print_hand(hand)
        print(Fore.WHITE + "Switching players...")
        time.sleep(3)
        clear()
