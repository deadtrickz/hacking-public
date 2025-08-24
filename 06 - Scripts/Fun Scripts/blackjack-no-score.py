import random

SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
    
    def add_card(self, card):
        self.cards.append(card)
        value_lookup = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
        self.value += value_lookup[card.rank]
        if card.rank == 'ace':
            self.ace = True

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def play(self):
        while True:
            # Show the player's hand
            print(f"Your hand: {self.player_hand.cards} ({self.player_hand.value})")
            print("")
            
            # Show the dealer's hand, but only show one card
            print(f"Dealer's hand: {self.dealer_hand.cards[0]} [hidden]")
            print("")
            
            # Ask the player if they want to hit or stand
            choice = input("Do you want to hit or stand? ")
            print("")
            if choice == 'hit':
                # Deal the player another card
                self.player_hand.add_card(self.deck.deal())
                # Check if the player has busted
                if self.player_hand.value > 21:
                    print("You have busted!")
                    print("")
                    return
            elif choice == 'stand':
                break
  
        print(f"Dealer's hand: {self.dealer_hand.cards} ({self.dealer_hand.value})")
        print("")
        while self.dealer_hand.value < 17:
            # Deal the dealer another card
            self.dealer_hand.add_card(self.deck.deal())
            print(f"Dealer's hand: {self.dealer_hand.cards} ({self.dealer_hand.value})")
            # Check if the dealer has busted
            if self.dealer_hand.value > 21:
                print("Dealer has busted!")
                print("")
                return
        
        if self.player_hand.value > self.dealer_hand.value:
            print("You win!")
            print("")
        elif self.player_hand.value < self.dealer_hand.value:
            print("You lose!")
            print("")
        else:
            print("It's a tie!")
            print("")

game = Blackjack()
game.play()

play_again = input("Do you want to play again? (y/n) ")
if play_again == 'y':
    game = Blackjack()
    game.play()