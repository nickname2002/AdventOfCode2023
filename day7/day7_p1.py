
# Input data containers (hand, bid_amount)
hands = []

# Card data containers
card_kinds = [
    [],         # One pair
    [],         # Two pairs
    [],         # Three of a kind
    [],         # Four of a kind
    []          # Full house
]

ordered_cards = []


# Read lines from input file
def read_input() -> None:
    input_file = open("day7/input.txt", "r")

    for line in input_file:
        fragments = line.split(" ")
        hands.append((fragments[0], int(fragments[1])))

    input_file.close()


def is_full_house(hand: str) -> bool:
    get_different_cards(hand) == 1


def is_four_of_a_kind(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    # Check if one card occurs four times
    for count in card_count.values():
        if count == 4:
            return True
        

def is_three_of_a_kind(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    # Check if one card occurs three times and no other card occurs twice
    for count in card_count.values():
        if count == 3 and len(card_count) == 3:
            return True


def is_two_pairs(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    # Check if two cards occur twice
    pair_count = 0
    for count in card_count.values():
        if count == 2:
            pair_count += 1

    return pair_count == 2


def is_one_pair(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    # Check if one card occurs twice
    for count in card_count.values():
        if count == 2:
            return True


# Get the number of different cards in a hand
def get_different_cards(hand: str) -> int:
    return len(set([*hand[0]]))


# Group cards into collections
def group_cards():
    global card_kinds
    for hand in hands:
        if is_full_house(hand[0]):
            card_kinds[4].append(hand)
        elif is_four_of_a_kind(hand[0]):
            card_kinds[3].append(hand)
        elif is_three_of_a_kind(hand[0]):
            card_kinds[2].append(hand)
        elif is_two_pairs(hand[0]):
            card_kinds[1].append(hand)
        elif is_one_pair(hand[0]):
            card_kinds[0].append(hand)


# Order hands from the most to the least valuable
def order_hands(hands: list) -> list:
    cards_and_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    # TODO: order hands by card values
    
    return hands


# Fill ordered_cards with the ordered hands
def fill_ordered_cards() -> None:
    global ordered_cards
    for i in range(5):
        ordered_cards += order_hands(card_kinds[i])


# Calculate the score of all hands
def calculate_score() -> int:
    global ordered_cards
    total_winnings = 0

    # Calculate the total winnings
    for i, (_, bid_amount) in enumerate(ordered_cards):
        total_winnings += bid_amount * (i + 1)

    return total_winnings


# Program entry point
read_input()
group_cards()
fill_ordered_cards()
print(calculate_score())