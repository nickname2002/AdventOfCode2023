
input_file = open("day12/input.txt", "r")

for line in input_file:

    # Derive different parts of the input string
    fragments = line.split(" ")
    hot_springs = fragments[0]
    group_sizes = [int(elem) for elem in fragments[1].split(",")]

    # TODO: Add stuff

input_file.close()