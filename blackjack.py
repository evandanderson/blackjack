import random

class Deck:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"] * 4


class Player:
    def __init__(self):
        self.hand = []


def deal(players,deck):
    while len(players[-1].hand) < 2:
        for player in players:
            player.hand.append(deck.cards.pop(0))


def hit(player,deck):
    player.hand.append(deck.cards.pop(0))


def shuffle(deck):
    random.shuffle(deck.cards)


def count(hand):
    total = 0
    for card in hand:
        if type(card) == int:
            total += card
        elif card in "JQK":
            total += 10

    aces = [card for card in hand if card == "A"]
    for i, ace in enumerate(aces):
        if total + 11 + len(aces) - (i + 1) <= 21:
            total += 11
        else:
            total += 1

    return total


def main():
    player, dealer = Player(), Player()
    deck = Deck()
    shuffle(deck)
    deal([dealer, player], deck)
    while count(dealer.hand) < 21 and count(player.hand) < 21 and not 17 <= count(dealer.hand) < count(player.hand) <= 21:
        print(f"""Your hand: {player.hand} ({count(player.hand)})\nDealer's hand: {dealer.hand} ({count(dealer.hand)})""")
        action = str(input("Your turn: ").lower())
        if action == "hit":
            hit(player, deck)
        if count(dealer.hand) <= 16:
            hit(dealer, deck)
    if count(player.hand) == 21 or 21 >= count(player.hand) > count(dealer.hand) or count(dealer.hand) > 21:
        print(f"***You win!***")
    else:
        print(f"You lost!")
    print(f"""Your hand: {player.hand} ({count(player.hand)})\nDealer's hand: {dealer.hand} ({count(dealer.hand)})""")
    

if __name__ == "__main__":
    main()