from collections import Counter
from functools import cmp_to_key
import sys


FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
TWO_OF_A_KIND = 2
HIGH_CARD = 1


CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS_JOKER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def key_type(hand: str) -> int:
    counts = list(Counter(hand).values())
    if 5 in counts:
        return FIVE_OF_A_KIND
    elif 4 in counts:
        return FOUR_OF_A_KIND
    elif 3 in counts and 2 in counts:
        return FULL_HOUSE
    elif 3 in counts:
        return THREE_OF_A_KIND
    elif counts.count(2) == 2:
        return TWO_PAIR
    elif 2 in counts:
        return TWO_OF_A_KIND
    else:
        return HIGH_CARD


def key_order(hand: str) -> list[int]:
    return [CARDS.index(card) for card in hand]


def key_type_joker(hand: str) -> int:
    # Instead of figuring it out manually, just replace the jokers by each of
    # the remaining cards and take the max score. This works because it's never
    # optimal to replace jokers with two different types of card.
    other_cards = set(hand.replace('J', ''))
    if other_cards:
        new_hands = set(hand.replace('J', card) for card in other_cards)
        return key_type(max(new_hands, key=key_type))
    else:
        # No other cards if the hand is all jokers.
        return FIVE_OF_A_KIND


def key_order_joker(hand: str) -> list[int]:
    return [CARDS_JOKER.index(card) for card in hand]


def score(hands: dict[str, int], key) -> int:
    ordered_hands = sorted(hands.keys(), key=key)
    total = 0
    for i, hand in enumerate(ordered_hands):
        rank = i + 1
        total += rank * hands[hand]
    return total


if __name__ == '__main__':
    hands = {}
    with open(sys.argv[1], 'r') as f:
        for line in f.read().splitlines():
            hand, bid = line.split()
            bid = int(bid)
            hands[hand] = bid
    key1 = lambda h: (key_type(h), key_order(h))
    key2 = lambda h: (key_type_joker(h), key_order_joker(h))
    print('part 1:', score(hands, key1))
    print('part 2:', score(hands, key2))