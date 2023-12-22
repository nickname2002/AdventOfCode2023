
map = []


# Move specific rock north until not possible
def move_rock(x: int, y: int) -> None:
    global map
    obstacles = ["O", "#"]

    # Return when already on top
    if y == 0:
        return

    offset_y = 1
    above_tile = map[y - offset_y][x]

    while True:

        # Base: stop when above tile is obstacle
        if above_tile in obstacles:
            break

        # Base: stop when border reached
        if y - offset_y < 0:
            break

        # Swap elems
        map[y - offset_y][x] = "O"
        map[y - offset_y + 1][x] = "."

        # Update tile above rock
        offset_y += 1
        above_tile = map[y - offset_y][x]


# Move all rocks to north as far as possible
def tilt_lever() -> None:
    global map
    for y, row in enumerate(map):
        for x, elem in enumerate(row):
            if elem == "O":
                move_rock(x, y)


def count_score() -> int:
    score = 0

    for y, row in enumerate(map):
        for elem in row:
            if elem == "O":
                score += len(map) - y

    return score


def visualize_map() -> None:
    global map
    print("=============================")
    for row in map:
        print(row)
    print("=============================")


def read_input() -> None:
    input_file = open("input.txt")

    for line in input_file:
        map.append([*line.strip()])

    input_file.close()

read_input()
visualize_map()
tilt_lever()
visualize_map()
print("Total load:", count_score())
