import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5, 'Six':6, 'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        print_cards = ''
        for card in self.deck:
            print_cards += '\n' + card.__str__()
        return f"The deck contains:{print_cards}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):

        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces >= 1:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        print(f"You Win {self.bet}")

    def lose_bet(self):
        self.total -= self.bet
        print(f"You Lose {self.bet}")


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("Place your bet"))
        except:
            print("Place your bet as a number")
        else:
            try:
                chips.bet < chips.total
            except:
                print("You don't have enough chips")
            else:
                print(f"Player bets {chips.bet}")
                break

def hit(deck, hand):
    hand.add_card(deck.deal_cards())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        player_choice = input("Choose h to hit or s to stand")

        if player_choice == 'h':
            hit(deck, hand)

        elif player_choice == "s":
            print("Player stands,. Dealer Plays.")
            playing = False

        else:
            print("Please try again")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(chips):
    chips.lose_bet()
    print("Over 21. You're bust, buster!")

def player_wins(chips):
    chips.win_bet()
    print(f"Player wins {chips.bet}")

def dealer_busts(chips):
    chips.win_bet()
    print(f"Dealer busted!\nPlayer wins {chips.bet}")

def dealer_wins(chips):
    chips.lose_bet()
    print("Dealer wins!")


if __name__ == '__main__':

    player_chips = Chips()

    while True:
        print("WELCOME TO BLACKJACK")
        print("Don't go over 21.")
        print("If there's a draw, the Dealer wins.")

        new_deck = Deck()
        new_deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(new_deck.deal_cards())
        player_hand.add_card(new_deck.deal_cards())

        dealer_hand = Hand()
        dealer_hand.add_card(new_deck.deal_cards())
        dealer_hand.add_card(new_deck.deal_cards())

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(new_deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break

        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                hit(new_deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_chips)

            elif player_hand.value > dealer_hand.value:
                player_wins(player_chips)

            elif player_hand.value <= dealer_hand.value:
                dealer_wins(player_chips)

        print(f"Your new chips total is {player_chips.total}")

        answer = input("Would you like to play again? y or n?\n\n")

        if answer == 'y':
            playing = True
            continue
        else:
            playing = False
            break

