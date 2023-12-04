
def main() -> None:
    file = open("day4/input.txt", "r")
    sum: int = 0

    # Iterate through each line in file
    for line in file:
        wn: list = get_winning_numbers(line)
        on: list = get_owning_numbers(line)
        sum += calc_score(wn, on)
    
    file.close()
    print(sum)


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