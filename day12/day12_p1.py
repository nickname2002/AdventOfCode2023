
input_file = open("day12/input.txt", "r")


def get_group_setup_in_hot_spring(hot_spring: str) -> list:
    groups_setup = []
    currently_in_group = False
    current_group_size = 0

    # Loop through hot spring
    for elem in hot_spring:

        # Case: seeing broken spring
        if elem == "#":
            currently_in_group = True
            current_group_size += 1
            continue
        
        # Case: not seeing broken spring
        if currently_in_group:
            groups_setup.append(current_group_size)
            current_group_size = 0
            currently_in_group = False

    # Track groups at the border of the hot spring
    if current_group_size != 0:
        groups_setup.append(current_group_size)

    return groups_setup


def produce_group_combinations(hot_spring: str, satisf_group_setup: str) -> list:
    combinations = []

    for i, elem in enumerate(hot_spring):
        if elem == "?":
            h = list(hot_spring)
            for j in ['.', '#']:
                h[i] = j
                combinations.append("".join(h))
                combinations.extend(produce_group_combinations("".join(h), satisf_group_setup))

    combinations = [c for c in combinations if not "?" in c]
    combinations = [c for c in combinations if get_group_setup_in_hot_spring(c) == satisf_group_setup]
    combinations = list(set(combinations))
    return combinations


for line in input_file:

    # Derive different parts of the input string
    fragments = line.split(" ")
    hot_springs = fragments[0]
    group_setup = [int(elem) for elem in fragments[1].split(",")]

    # TODO: Add stuff
    print(produce_group_combinations(hot_springs, group_setup))

input_file.close()