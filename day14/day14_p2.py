import copy

rock_map = []

# Move specific rock north until not possible
def move_rocks_north() -> None:
    global rock_map
    obstacles = ["O", "#"]

    for y, row in enumerate(rock_map):
        for x, elem in enumerate(row):
            if elem == "O":

                # Return when already on top
                if y == 0:
                    continue

                offset_y = 1
                above_tile = rock_map[y - offset_y][x]

                while True:

                    # Base: stop when above tile is obstacle
                    if above_tile in obstacles:
                        break

                    # Base: stop when border reached
                    if y - offset_y < 0:
                        break

                    # Swap elems
                    rock_map[y - offset_y][x] = "O"
                    rock_map[y - offset_y + 1][x] = "."

                    # Update tile above rock
                    offset_y += 1
                    above_tile = rock_map[y - offset_y][x]


def move_rocks_south() -> None:
    global rock_map
    rock_map.reverse()
    move_rocks_north()
    rock_map.reverse()


def move_rocks_east() -> None:
    global rock_map

    for row in rock_map:
        row.reverse()

    move_rocks_west()

    for row in rock_map:
        row.reverse()


def move_rocks_west() -> None:
    global rock_map
    obstacles = ["O", "#"]

    for y, row in enumerate(rock_map):
        for x, elem in enumerate(row):
            if elem == "O":

                # Return when already on left
                if x == 0:
                    continue

                offset_x = 1
                left_tile = rock_map[y][x - 1]

                while True:

                    # Base: stop when left tile is obstacle
                    if left_tile in obstacles:
                        break

                    # Base: stop when border reached
                    if x - offset_x < 0:
                        break

                    # Swap elems
                    rock_map[y][x - offset_x] = "O"
                    rock_map[y][x - offset_x + 1] = "."

                    # Update tile above rock
                    offset_x += 1
                    left_tile = rock_map[y][x - offset_x]


# TODO: Not working yet -> Cycle detection needs work
def tilt_lever(total_amount = 1) -> None:
    map_results = []

    while True:
        move_rocks_north()
        move_rocks_west()
        move_rocks_south()
        move_rocks_east()

        if rock_map in map_results:
            break

        map_results.append(copy.deepcopy(rock_map))

    cycle_length = len(map_results)
    print("Length of cycle:", cycle_length)
    amount_to_tilt = total_amount % cycle_length
    print("Amount to tilt left:", amount_to_tilt)

    for i in range(amount_to_tilt):
        move_rocks_north()
        move_rocks_west()
        move_rocks_south()
        move_rocks_east()


def count_score() -> int:
    score = 0

    for y, row in enumerate(rock_map):
        for elem in row:
            if elem == "O":
                score += len(rock_map) - y

    return score


def visualize_map() -> None:
    global rock_map
    print("=============================")
    for row in rock_map:
        print(row)
    print("=============================")


def read_input() -> None:
    input_file = open("input.txt")

    for line in input_file:
        rock_map.append([*line.strip()])

    input_file.close()

read_input()
tilt_lever(1000000000)
print("Total load:", count_score())
