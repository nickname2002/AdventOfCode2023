
class Card:

    def __init__(self, id, wn, on):
        self.id = id
        self.winning_numbers = wn
        self.owning_numbers = on        

    # Get matching numbers from two lists
    def get_matching_numbers(self) -> list:
        return list(set(self.winning_numbers).intersection(set(self.owning_numbers)))


def main() -> None:
    available_cards: list = make_card_objects()
    holding_cards: dict = {}
    cards_in_output: list = []

    # Fill dictionary
    for card in available_cards:
        holding_cards[card.id] = 1

    # Fill cards_in_output
    for i in range(len(available_cards)):
        while (holding_cards[i] > 0):
            matching_numbers = available_cards[i].get_matching_numbers()

            # Handle case where no matches
            if len(matching_numbers) == 0:
                holding_cards[i] -= 1
                cards_in_output.append(i)
                continue

            # Handle case where there are matches
            for j in range(len(matching_numbers)):
                holding_cards[i + j + 1] += 1

            # Remove current card from holding cards
            cards_in_output.append(i)
            holding_cards[i] -= 1


    # Print output
    print(len(cards_in_output))


# Create new card objects from file
def make_card_objects() -> list:
    card_objects: list = []
    file = open("day4/input.txt", "r")

    # Iterate through each line in file
    for i, line in enumerate(file):
        wn: list = get_winning_numbers(line)
        on: list = get_owning_numbers(line)
        card_objects.append(Card(i, wn, on))
    
    file.close()
    return card_objects
    

# Get winning numbers for a specific line
def get_winning_numbers(line: str) -> list:
    winning_numbers = line.split("|")[0].split(":")[1].split(" ")
    
    # Remove all spaces from winning numbers
    while (winning_numbers.__contains__('')):
        winning_numbers.remove('')

    # Convert all winning number strings to ints
    for i in range(len(winning_numbers)):
        winning_numbers[i] = int(winning_numbers[i])

    return winning_numbers


# Get owning numbers for a specific line
def get_owning_numbers(line: str) -> list:
    owning_numbers = line.split("|")[1].split(' ')

    # Remove spaces from owning numbers
    while (owning_numbers.__contains__('')):
        owning_numbers.remove('')

    # Convert all owning number strings to ints
    for i in range(len(owning_numbers)):
        owning_numbers[i] = int(owning_numbers[i])

    return owning_numbers


def order_on_id(card_list: [Card]) -> list: 
    return sorted(card_list, key=lambda x: x.id, reverse=True)
  


# Calculate score of specific set of winning & owning numbers
def calc_score(winning_numbers: list, owning_numbers: list) -> int:
    points: int = 0

    # Calculate points from owning numbers
    for number in owning_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    return points


main()