import copy

grid: list = []
starting_position: tuple = None
states_found = []


# Read the grid from the input file
def read_grid() -> None:
    global grid, starting_position
    input_file = open("day10/input.txt", "r")

    for y, line in enumerate(input_file):
        row = [*line.strip()]

        # Search for starting position
        if row.__contains__("S"):
            for x, tile in enumerate(row):
                if tile == "S":
                    starting_position = (x, y)

        grid.append(row)

    input_file.close()


# Move left operation
def move_left(state: list, pos: tuple) -> (list, tuple):
    # Base case: at the border of the grid.
    if pos[0] == 0:
        return (state, pos)
    
    current_tile = state[pos[1]][pos[0]]
    left_tile = state[pos[1]][pos[0] - 1]

    # Case: no valid tile to move
    if left_tile != "-" and left_tile != "F" and left_tile != "L":
        return (state, pos)
    
    # Modify grid
    modified_state = state.copy()
    modified_state[pos[1]][pos[0] - 1] = current_tile + 1

    # Modify position
    modified_pos = (pos[0] - 1, pos[1])

    return (modified_state, modified_pos)


# Move right operation
def move_right(state: list, pos: tuple) -> (list, tuple):
    # Base case: at the border of the grid.
    if pos[0] == len(state[pos[1]]):
        return (state, pos)
    
    current_tile = state[pos[1]][pos[0]]
    right_tile = state[pos[1]][pos[0] + 1]

    # Case: no valid tile to move
    if right_tile != "-" and right_tile != "7" and right_tile != "J":
        return (state.copy(), pos)
    
    # Modify grid
    modified_state = state.copy()
    modified_state[pos[1]][pos[0] + 1] = current_tile + 1

    # Modify position
    modified_pos = (pos[0] + 1, pos[1])

    return (modified_state, modified_pos)


# Move right operation
def move_up(state: list, pos: tuple) -> (list, tuple):
    # Base case: at the border of the grid.
    if pos[1] == 0:
        return (state, pos)
    
    current_tile = state[pos[1]][pos[0]]
    up_tile = state[pos[1] - 1][pos[0]]

    # Case: no valid tile to move
    if up_tile != "F" and up_tile != "|" and up_tile != "7":
        return (state, pos)
    
    # Modify grid
    modified_state = state.copy()
    modified_state[pos[1] - 1][pos[0]] = current_tile + 1

    # Modify position
    modified_pos = (pos[0], pos[1] - 1)

    return (modified_state, modified_pos)


# Move down operation
def move_down(state: list, pos: tuple) -> (list, tuple):
    # Base case: at the border of the grid.
    if pos[0] >= len(state) - 1:
        return (state, pos)
    
    current_tile = state[pos[1]][pos[0]]
    down_tile = state[pos[1] + 1][pos[0]]

    # Case: no valid tile to move
    if down_tile != "|" and down_tile != "L" and down_tile != "J":
        return (state, pos)
    
    # Modify grid
    modified_state = state.copy()
    modified_state[pos[1] + 1][pos[0]] = current_tile + 1

    # Modify position
    modified_pos = (pos[0], pos[1] + 1)

    return (modified_state, modified_pos)


# Returns whether no new state has been found
def no_new_state_found(s0: list, s1: list, s2: list, s3: list, s4: list) -> bool:
    return \
        s0 == s1 and \
          s0 == s2 and \
            s0 == s3 and \
                s0 == s4


def generate_new_states(state: list, pos: tuple) -> list:
    states = []
    states.append(move_left(copy.deepcopy(state), pos))
    states.append(move_right(copy.deepcopy(state), pos))
    states.append(move_up(copy.deepcopy(state), pos))
    states.append(move_down(copy.deepcopy(state), pos))
    return states


def find_new_state(state: list, pos: tuple) -> None:
    global states_found
    states = generate_new_states(state, pos)
    states = [(s, p) for s, p in states if s != state]

    if len(states) == 0:
        return state
    
    for s, p in states:
        states_found.append(find_new_state(s, p))


def visualize_grid(grid: list):
    print("=========================")
    if grid == None:
        return
    for row in grid:
        print(row)
    print("=========================")


# Program entry point
read_grid()
grid[starting_position[1]][starting_position[0]] = 0
find_new_state(grid.copy(), starting_position)
states_found = [s for s in states_found if s != None]
for state in states_found:
    visualize_grid(state)