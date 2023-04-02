############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
###############################################################

# Importing necessary libraries for performance
from os import system
from project_art import logo
import random


def hit_card(card, cards):
    """
    Appends a random card from the deck of cards passed.
    """
    card.append(random.choice(cards))


def final_hand(cards, string):
    """
    Displays the final hand of a player with its final score

    Args:
        cards (list): A list for deck of card
        string (str): Name of a player, either user or computer
    """
    print(f"{string} final hand: {cards}, final score: {sum(cards)}")


def calculate_score(cards):
    """
    Takes the list of cards and returns the total score of player

    Args:
        cards (list): A list for deck of cards
    """

    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def display_winner(players_final, computers_final):
    """
    Displays the appropriate message that what is the decision of game by comparing the player and computer's score

    Args:
        players_final (int): players final score at the end of game
        computers_final (int): computers final score at the end of game
    """
    if players_final == computers_final:
        print("Draw 😀")
    elif computers_final == 0:
        print("Opponent has a Blackjack. You Loose 😢")
    elif players_final == 0:
        print("You have a Blackjack. You Win! 😁")
    elif players_final > 21:
        print("You went over. You Loose 😢")
    elif computers_final > 21:
        print("Opponent went over. You Win! 😁")
    elif players_final > computers_final:
        print("You Win! 😁")
    else:
        print("You Loose 😢")


def game():
    """
    Runs the game and perform all operations in it. 
    """

    # Prints the game logo at the start
    print(logo)

    # Initializes a list for player and computer cards
    player_cards = []
    computer_cards = []

    # Hit 2 cards for both player and computer
    for _ in range(2):
        hit_card(card=player_cards, cards=cards)
        hit_card(card=computer_cards, cards=cards)

    # Compute the computer's score and store it in a variable
    computer_score = calculate_score(cards=computer_cards)

    # Run the loop till player is drawing a card
    while True:
        # Calculate and update the player's score at the beginning of each iteration
        player_score = calculate_score(cards=player_cards)

        # Display the players and computers information
        print("\n[+] Displaying Player's information and Computer First Card:")
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        # Terminate if the player or computer has a blackjack or player went over
        if player_score > 21 or player_score == 0 or computer_score == 0:
            break

        # Ask user for next card hitting otherwise
        else:
            continue_or_pass = input(
                "Type 'y' to get another card, type 'n' to pass: ")

            # Hit card if user wishes to hit card
            if continue_or_pass == 'y':
                hit_card(card=player_cards, cards=cards)
            # Otherwise terminate
            else:
                break

    # Computer's turn will execute after the players turn
    # Computer will draw until its score crosses 16 or it has a blackjack
    while computer_score != 0 and computer_score < 17:
        hit_card(card=computer_cards, cards=cards)
        computer_score = calculate_score(computer_cards)

    # Display the final hand of computer and player at the end of the game
    print("\n[+] Displaying Final Hand Information:")
    final_hand(cards=player_cards, string="Your")
    final_hand(cards=computer_cards, string="Computer's")

    # Display the result at the end of the game
    print("\n[+] Displaying Result:")
    display_winner(players_final=player_score, computers_final=computer_score)
    print()

    # Ask user to replay the game
    play_again = input(
        "Do you want to play Blackjack again? Type 'y' or 'n': ")

    # The game will start over if the user wishes to play the game (presses y)
    if play_again == 'y':
        system("cls")
        game()


# Main method that will call the game() at first.
if __name__ == "__main__":

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play = input("Do you want to play a game of Blacjack? Type 'y' or 'n': ")

    system("cls") if play == "y" else exit(0)
    game()
