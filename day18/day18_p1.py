
dig_plan = [["#"]]
current_pos: tuple = (0, 0)


def dig_right():
    global current_pos, dig_plan

    # Add new '.' to all dig_plan rows
    if current_pos[0] == len(dig_plan[0]) - 1:
        for row in range(len(dig_plan)):
            dig_plan[row].append(".")

    # Apply digging
    dig_plan[current_pos[1]][current_pos[0] + 1] = "#"
    current_pos = (current_pos[0] + 1, current_pos[1])


def dig_left():
    global current_pos, dig_plan

    # Insert new '.' to all dig_plan rows at index 0
    if current_pos[0] == 0:
        for i in range(len(dig_plan)):
            dig_plan[i].insert(0, ".")

        # Apply digging
        dig_plan[current_pos[1]][current_pos[0]] = "#"
        return

    # Apply digging
    dig_plan[current_pos[1]][current_pos[0] - 1] = "#"
    current_pos = (current_pos[0] - 1, current_pos[1])


def dig_up():
    global current_pos, dig_plan

    # Add row when necessary
    if current_pos[1] == 0:
        row_to_add = ["." for i in range(len(dig_plan[0]))]
        dig_plan.insert(0, row_to_add)
        dig_plan[current_pos[1]][current_pos[0]] = "#"
        return

    # Apply digging
    dig_plan[current_pos[1] - 1][current_pos[0]] = "#"
    current_pos = (current_pos[0], current_pos[1] - 1)


def dig_down():
    global current_pos, dig_plan

    # Add new row when necessary
    if current_pos[1] + 1 == len(dig_plan):
        row_to_add = ["." for i in range(len(dig_plan[0]))]
        dig_plan.append(row_to_add)
        dig_plan[current_pos[1]][current_pos[0]] = "#"

    # Apply digging
    dig_plan[current_pos[1] + 1][current_pos[0]] = "#"
    current_pos = (current_pos[0], current_pos[1] + 1)


def visualize_dig_plan():
    for row in dig_plan:
        print(row)
    print("======================")


def perform_operation(operation, amount: int):
    for i in range(amount):
        operation()


def determine_capacity() -> int:
    global dig_plan

    total_area = 0

    # TODO: constantly check for containing another "#", then add +1 from start seeing thing

    return total_area


# Entry point
input_file = open("input.txt", "r")

for line in input_file:
    fragments = line.split(" ")
    operation = fragments[0]
    amount = int(fragments[1])

    # Perform operation
    if operation == "R":
        perform_operation(dig_right, amount)
    elif operation == "D":
        perform_operation(dig_down, amount)
    elif operation == "L":
        perform_operation(dig_left, amount)
    else:
        perform_operation(dig_up, amount)

input_file.close()
dig_plan = transform_grid(dig_plan)
visualize_dig_plan()
print(determine_capacity())
