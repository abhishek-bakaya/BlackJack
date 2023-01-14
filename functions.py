from os import system
from classes import title

# Functions-----------------------------------------------------------------------------------------------------

def cls():
    _ = system('cls')
# -------------------------------------------------------------------------------------------------

def begin():
    ready = None
    cls()
    print(f"{title}\n")
    print("How to play:\n" +
          "-There are 2 players in the game - Dealer (computer) and Player (human).\n" +
          "-Both the players will be served 2 cards initially; Dealer's only one card will be exposed to the Player.\n" +
          "-Player will be asked to place bet with only 2 cards in the hand.\n" +
          "-Player's goal is to keep the sum of the hand less than or equal to 21 and more than the Dealer.\n" +
          "-Player will get first turn and will be asked to hit or stand; if you want to draw another card, type 'hit' else type 'stand'.\n" +
          "-If the sum exceeds 21, the Player is busted and loses the game.\n" +
          "-Player will get the double amount of the bet placed if wins the hand, and lose the amount if loses the hand.\n")
    
    while ready not in ('yes', 'no'):
        ready = input("Are you ready? (yes/no): ").lower().strip()
    
    return(ready)
# -------------------------------------------------------------------------------------------------

def replay():
    
    ready = None
    while ready not in ('yes', 'no'):
        ready = input("\nPlay another hand? (yes/no): ").lower().strip()
    return ready
# -------------------------------------------------------------------------------------------------

def display(dealer, player, stand, game):
    
    cls()
    print(f"{title}\t\t\t\tGame: {game}  |  " +\
          f"Current position: ₹{player.chips.total-player.chips.bet}  |  " +\
          f"At stake: ₹{player.chips.bet}\n\n" +\
          f"Dealer's Hand:\n\t\t", end='')
    
    if stand:
        print(*dealer.hand.cards, sep='\n\t\t')
        print(f"\nDealer's Hand = {dealer.hand.value}")
    
    elif not stand:
        print(f"{dealer.hand.cards[0]}\n\t\t<card hidden>")
    
    print("\n\nPlayer's Hand:\n\t\t", end='')
    print(*player.hand.cards, sep='\n\t\t')
    print(f"\nPlayer's Hand = {player.hand.value}")
# -------------------------------------------------------------------------------------------------

def end_game(dealer, player, stand, game):
    if dealer.hand.value > 21:
        display(dealer, player, stand, game)
        player.chips.win_bet()
        print("\nDealer busted. You won.")
    
    elif dealer.hand.value > player.hand.value:
        display(dealer, player, stand, game)
        player.chips.lose_bet()
        print("\nDealer won.")
    
    elif player.hand.value > dealer.hand.value:
        display(dealer, player, stand, game)
        player.chips.win_bet()
        print("\nYou won.")
    
    elif player.hand.value == dealer.hand.value:
        display(dealer, player, stand, game)
        print("\nIt's a tie. No profit - No loss.")
    
    return replay()