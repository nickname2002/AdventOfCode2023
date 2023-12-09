histories = []


# Read histories from input file
def read_histories() -> None:
    global histories
    input_file = open("day9/input.txt", "r")

    for line in input_file:
        list_with_chars = line.split(" ")
        list_with_numbers = [int(numb) for numb in list_with_chars] 
        histories.append(list_with_numbers)

    input_file.close()


# Get list of differences between items in a list
def get_diff_in_seq(seq: list) -> list:
    pass


# Get next value in sequence of history
def get_next_value_in_seq(hist: list) -> list:
    pass


# Program entry point
read_histories()
sum_of_next_items = 0

for hist in histories:
    sum_of_next_items += get_next_value_in_seq(hist)

print(sum_of_next_items)