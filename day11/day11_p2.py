
space = []
galaxy_amount = 0
pairs_of_distances = {}
dist_after_rows = []
dist_after_cols = []

# Read galaxy from input file
def read_galaxy() -> None:
    global dist_after_rows, dist_after_cols
    input_file = open("day11/input.txt", "r")

    for line in input_file:
        space.append([*line.strip()])

    dist_after_rows = [0 for _ in space[0]]
    dist_after_cols = [0 for _ in space]

    input_file.close()


def expand_galaxy() -> None:
    global space, dist_after_rows, dist_after_cols
    expansion_size = 999999

    # Expand columns
    column_index = 0
    column_amount = len(space[0])
    while column_index < column_amount:
        column = [row[column_index] for row in space]
        
        # Handle empty columns
        if len(set(column)) == 1:
            dist_after_cols[column_index] += expansion_size

        column_index += 1

    # Expand rows
    row_index = 0
    while row_index < len(space):

        # Handle empty rows
        if len(set(space[row_index])) == 1:
            dist_after_rows[row_index] += expansion_size

        row_index += 1    


def calc_distance_between_galaxies(g1: str, g2: str) -> int:
    global space, dist_after_rows, dist_after_cols

    pos_g1 = ()
    pos_g2 = ()

    # Get positions of galaxies
    for y, row in enumerate(space):
        for x, elem in enumerate(row):
            if elem == g1:
                pos_g1 = (x, y)
            elif elem == g2:
                pos_g2 = (x, y)

    extra_dist_x = 0
    extra_dist_y = 0

    # Calculate extra dist x
    for i in range(min(pos_g1[0], pos_g2[0]), max(pos_g1[0], pos_g2[0])):
        extra_dist_x += dist_after_cols[i]

    # Calculate extra dist y
    for i in range(min(pos_g1[1], pos_g2[1]), max(pos_g1[1], pos_g2[1])):
        extra_dist_y += dist_after_rows[i]

    # Calculate difference in x and y
    x_diff = max(pos_g1[0], pos_g2[0]) - min(pos_g1[0], pos_g2[0]) + extra_dist_x
    y_diff = max(pos_g1[1], pos_g2[1]) - min(pos_g1[1], pos_g2[1]) + extra_dist_y

    return x_diff + y_diff


def number_galaxies_in_space() -> None:
    global space
    global galaxy_amount
    galaxy_id = 1

    # Fill space with ids
    for y, row in enumerate(space):
        for x, elem in enumerate(row):
            if elem == "#":
                space[y][x] = str(galaxy_id)
                galaxy_id += 1

    galaxy_amount = galaxy_id - 1    


def form_pairs_of_distances():
    global pairs_of_distances

    # Form pairs for each galaxy
    for id1 in range(1, galaxy_amount + 1):
        id2 = id1 + 1
        
        # Only make pairs with higher galaxies
        while id2 <= galaxy_amount:
            dist = calc_distance_between_galaxies(str(id1), str(id2))
            pairs_of_distances[(id1, id2)] = dist 
            id2 += 1


def visualize_galaxy() -> None:
    global space
    print("=====================")
    for row in space:
        print(row)
    print("=====================")


# Program entry point
read_galaxy()
print("> Done reading space")
expand_galaxy()
print("> Done expanding space")
number_galaxies_in_space()
print("> Done numbering galaxies")
form_pairs_of_distances()
print("> Done forming pairs of distances.")
print("Sum of distances: ", sum([v for v in pairs_of_distances.values()]))
