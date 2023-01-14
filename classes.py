import random

# Global variables----------------------------------------------------------------------------------------------
title = 'BlackJack'
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,\
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Class definitions---------------------------------------------------------------------------------------------

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
# -------------------------------------------------------------------------------------------------

class Deck:

    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop(0)
# -------------------------------------------------------------------------------------------------

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_aces(self):
        while self.aces and self.value>21:
            self.value -= 10
            self.aces -= 1
# -------------------------------------------------------------------------------------------------

class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0
    
    def lose_bet(self):
        self.total -= self.bet
    
    def win_bet(self):
        self.total += self.bet
# -------------------------------------------------------------------------------------------------

class Player():

    def __init__(self, name = 'Dealer'):
        self.name = name
        self.chips = Chips()
        self.hand = Hand()
    
    def make_bet(self):
        
        print(f"\nAvailable chips worth: ₹{self.chips.total}")
        while True:
            
            try:
                bet = int(input("Your bet worth: ₹"))
            except ValueError:
                print("\nInvalid input!!!\n")
            else:
                if bet == 0:
                    print("\nIt's not a friendly game.")
                elif bet > self.chips.total:
                    print(f"\nNot enough chips.\nAvailable chips worth: ₹{self.chips.total}")
                    continue
                else:
                    self.chips.bet = bet
                    break
        
    
    def hit_or_stand(self, deck):
        
        stand = False
        while True:
            choice = input("\n\nHit or Stand: ").lower()
        
            if choice == 'hit':
                self.hit(deck)            
            elif choice == 'stand':
                stand = True
            else:
                print("Type 'hit' or 'stand': ")
                continue
            break
        
        return stand

    def hit(self, deck):
        card = deck.deal()
        self.hand.add_card(card)
        self.hand.adjust_for_aces()
    
    def reset(self):
        self.hand.cards.clear()
        self.hand.value = 0
        self.chips.bet = 0
        self.hand.aces = 0
