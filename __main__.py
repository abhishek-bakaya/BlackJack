from classes import title, Deck, Player
from functions import begin, display, end_game, replay

# -------------------------------------------------------------------------------------------------

def main():

    ready = begin()
    game = 0

    while ready == 'yes':
        
        game += 1

        if game == 1:
            dealer = Player()
            player = Player('Player')
        else:
            dealer.reset()
            player.reset()
        deck = Deck()
        deck.shuffle()
        stand = False

        if not player.chips.total:
            print("You don't have anything to bet. You can't play anymore.")
            break

        for _ in range(2):
            dealer.hit(deck)
            player.hit(deck)
        
        display(dealer, player, stand, game)
        player.make_bet()
        while not stand:

            display(dealer, player, stand, game)
            stand = player.hit_or_stand(deck)

            if player.hand.value > 21:
                player.chips.lose_bet()
                display(dealer, player, stand, game)
                print("\nYou busted. Dealer won.")
                ready = replay()
                break

            if stand:
                display(dealer, player, stand, game)             
                while dealer.hand.value < 17:
                    dealer.hit(deck)
                
                ready = end_game(dealer, player, stand, game)

if __name__ == '__main__': main()
