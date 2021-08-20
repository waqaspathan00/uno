from colorama import Fore
from os import system, name
import time, random


def print_card_in_color(card):
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
    for i, card in enumerate(hand):
        print(Fore.WHITE + "[" + str(i) + "] - ", end="")
        print_card_in_color(card)
    print()


def play_card(position, hand):
    card = hand[position]
    if card == "Draw":
        new_card = cards.pop()
        hand.append(new_card)
        return card_in_play
    del hand[position]
    return card


def validate_card(card_in_play, hand, card_choice_index):
    card_choice = hand[card_choice_index]

    if card_choice == "Draw":
        return True
    elif card_in_play[0] == card_choice[0]:
        return True
    elif card_in_play[1] == card_choice[1]:
        return True
    else:
        return False


def clear():
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
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]

random.shuffle(cards)

cards_per_hand = 7
players = 2
hands = []
for i in range(players):
    hand = [cards.pop() for j in range(cards_per_hand)]
    hand.insert(0, "Draw")
    hands.append(hand)

card_in_play = cards.pop()

running = True
while running:
    for i, hand in enumerate(hands):
        print(Fore.WHITE + "Current card in play: ", end="")
        print_card_in_color(card_in_play)
        print_hand(hand)
        card_choice_index = int(input(Fore.WHITE + "Player " + str(i + 1) + ", enter what card you want to play: "))
        while not validate_card(card_in_play, hand, card_choice_index):
            print("Incorrect choice")
            card_choice_index = int(input(Fore.WHITE + "Player " + str(i + 1) + ", enter what card you want to play: "))

        card_in_play = play_card(card_choice_index, hand)

        if len(hand) == 1:
            running = False
            print("Player " + str(i + 1) + " wins!")
            print("Ending Game...")
            break

        print_hand(hand)
        print(Fore.WHITE + "Switching players...")
        time.sleep(3)
        clear()
