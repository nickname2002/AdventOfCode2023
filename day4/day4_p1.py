
def main() -> None:
    file = open("day4/input.txt", "r")

    # Iterate through each line in file
    for line in file:
        wn: list = get_winning_numbers()
        on: list = get_owning_numbers()

        # TODO: more implementation.

    file.close()


# Get winning numbers for a specific line
def get_winning_numbers(line: str) -> list:
    pass


# Get owning numbers for a specific line
def get_owning_numbers(line: str) -> list:
    pass


# Calculate score of specific set of winning & owning numbers
def calc_score(winning_numbers: list, owning_numbers: list) -> int:
    pass


main()