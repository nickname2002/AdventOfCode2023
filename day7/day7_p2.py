# Input data containers (hand, bid_amount)
hands = []

# Card data containers
card_kinds = [
    [],         # High card
    [],         # One pair
    [],         # Two pairs
    [],         # Three of a kind
    [],         # Full house
    [],         # Four of a kind
    [],         # Five of a kind
]

ordered_cards = []


# Read lines from input file
def read_input() -> None:
    input_file = open("day7/input.txt", "r")

    for line in input_file:
        fragments = line.split(" ")
        hands.append((fragments[0], int(fragments[1])))

    input_file.close()


def correct_counts_with_jokers(card_count: dict) -> dict:

    # Return if the dict doesn't contain any jokers
    if not list(card_count.keys()).__contains__("J"):
        return card_count
    
    # Also return if there are 5 jokers
    if card_count["J"] == 5:
        return card_count

    # Get amount of jokers and remove from dict
    jokers = card_count["J"]
    card_count.pop("J")

    # Get highest card in the dictionary
    highest = None

    for i, card in enumerate(list(card_count.keys())):
        if i == 0:
            highest = card

        if card_count[card] > card_count[highest]:
            highest = card

    # Update the highest card with the joker amount
    card_count[highest] += jokers
    return card_count


def is_full_house(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_count = correct_counts_with_jokers(card_count)

    # Check if one card occurs four times
    if set(card_count.values()).__contains__(3) and \
        set(card_count.values()).__contains__(2):
        return True
    
    return False


def is_five_of_a_kind(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_count = correct_counts_with_jokers(card_count)

    # Check if one card occurs three times and no other card occurs twice
    if set(card_count.values()).__contains__(5):
        return True 
    
    return False


def is_four_of_a_kind(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_count = correct_counts_with_jokers(card_count)

    # Check if one card occurs four times
    for count in card_count.values():
        if count == 4:
            return True
        

def is_three_of_a_kind(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_count = correct_counts_with_jokers(card_count)

    # Check if one card occurs three times and no other card occurs twice
    for count in card_count.values():
        if count == 3 and len(card_count) == 3:
            return True


def is_two_pairs(hand: str) -> bool:
    card_count = {}

    # Count the occurrences of each card
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    card_count = correct_counts_with_jokers(card_count)

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

    card_count = correct_counts_with_jokers(card_count)

    # Check if one card occurs twice
    for count in card_count.values():
        if count == 2:
            return True


# Group cards into collections
def group_cards():
    global card_kinds
    for hand in hands:
        if is_five_of_a_kind(hand[0]):
            card_kinds[6].append(hand)

        elif is_four_of_a_kind(hand[0]):
            card_kinds[5].append(hand)
        
        elif is_full_house(hand[0]):
            card_kinds[4].append(hand)

        elif is_three_of_a_kind(hand[0]):
            card_kinds[3].append(hand)

        elif is_two_pairs(hand[0]):
            card_kinds[2].append(hand)

        elif is_one_pair(hand[0]):
            card_kinds[1].append(hand)

        else:
            card_kinds[0].append(hand)


# Order hands from the most to the least valuable
def order_hands(hands: list) -> list:
    n = len(hands)

    # Use 'Insertion Sort met de Deur' technique
    if n <= 1:
        print(hands)
        return hands
    
    for i in range(1, n):
        sel_hand = hands[i]
        j = i - 1
        
        while j >= 0 and is_stronger_hand(sel_hand[0], hands[j][0]):
            hands[j + 1] = hands[j]
            j -= 1
        
        hands[j + 1] = sel_hand

    hands.reverse()
    return hands


# Returns whether the first hand is stronger than the second hand.
def is_stronger_hand(h1: list, h2: list) -> bool:
    cards_and_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1
    }

    for i in range(len(h1)):
        card_value_h1 = cards_and_values[h1[i]]
        card_value_h2 = cards_and_values[h2[i]]
        if card_value_h1 > card_value_h2:
            return True 
        elif card_value_h1 < card_value_h2:
            return False
        
    return False


# Fill ordered_cards with the ordered hands
def fill_ordered_cards() -> None:
    global ordered_cards
    for i, _ in enumerate(card_kinds):
        ordered_cards.extend(order_hands(card_kinds[i]))


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