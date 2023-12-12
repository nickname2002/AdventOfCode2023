
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


def produce_group_combinations(hot_spring: str, satisf_group_setup: str, start_index=0) -> list:
    combinations = []

    for i in range(start_index, len(hot_spring)):
        if hot_spring[i] == "?":

            # Produce all combinations
            for j in ['.', '#']:
                h = list(hot_spring)
                h[i] = j

                # Case: hot spring production is complete
                if "?" not in h:
                    if get_group_setup_in_hot_spring("".join(h)) == satisf_group_setup:
                        combinations.append("".join(h))
                else:
                    combinations.extend(produce_group_combinations("".join(h), satisf_group_setup, i + 1))
    
    return combinations


input_file = open("day12/input.txt", "r")
total_sum = 0

for i, line in enumerate(input_file):
    print("Line: ", i)

    # Derive different parts of the input string
    fragments = line.split(" ")
    hot_springs = fragments[0]
    group_setup = [int(elem) for elem in fragments[1].split(",")]

    # Produce result to add to sum
    res = produce_group_combinations(hot_springs, group_setup)
    total_sum += len(res)

print(total_sum)
input_file.close()