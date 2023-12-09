histories = []


# Read histories from input file
def read_histories() -> None:
    global histories
    input_file = open("day9/input.txt", "r")

    for line in input_file:
        list_with_chars = line.split(" ")
        list_with_numbers = [int(numb) for numb in list_with_chars] 
        list_with_numbers.reverse()
        histories.append(list_with_numbers)

    input_file.close()


# Get list of differences between items in a list
def get_diff_in_seq(seq: list) -> list:
    diff = []
    for i in range(len(seq) - 1):
        diff.append(seq[i + 1] - seq[i])

    return diff


# Get next value in sequence of history
def get_next_value_in_seq(hist: list) -> list:
    differences = [get_diff_in_seq(hist)]

    # Fill differences list
    while True:
        current_diff = get_diff_in_seq(differences[-1])
        differences.append(current_diff)

        # Check whether current_diff contains only 0's        
        if all([v == 0 for v in current_diff]):
            break

    # Calculate next value in the sequence
    differences.reverse()
    to_add = 0
    for diff in differences:
        to_add = diff[-1] + to_add

    return hist[-1] + to_add


# Program entry point
read_histories()
sum_of_next_items = 0

for hist in histories:
    sum_of_next_items += get_next_value_in_seq(hist)

print(sum_of_next_items)