import math

# Traversing operations
operations = []

# Dict: (source, destination)
locations = {}
current_locations = []


# Read locations from input file.
def read_locations() -> None:
    global operations, locations
    input_file = open("day8/input.txt", "r")

    for i, line in enumerate(input_file):

        # Read operations
        if i == 0:
            operations = [*line.strip()]

        # Read locations
        if i >= 2:
            fragments = line.split(" = ")
            tuple_fragment = fragments[1].split(", ")
            
            # Create destination locations
            first_loc = tuple_fragment[0].removeprefix("(")
            second_loc = tuple_fragment[1].removesuffix(")").replace(")", "").strip()
            
            # Add location
            locations[fragments[0]] = [
                first_loc,
                second_loc
            ]

        

# Fill starting locations list
def get_starting_locations() -> None:
    global locations, current_locations

    for location in locations.keys():
        if location[-1] == "A":
            current_locations.append(location)


# Get whether all locations end with 'Z'
def all_locations_end_with_z() -> bool:
    global current_locations

    for location in current_locations:
        if location[-1] != "Z":
            return False

    return True


# Traverse all locations in list with a specific operation
def traverse_all_locations(operation: str) -> None:
    global current_locations, locations

    for i, loc in enumerate(current_locations):
        if operation == "L":
            current_locations[i] = locations[loc][0]
        else:
            current_locations[i] = locations[loc][1]


# Get number of steps to reach "ZZZ" from the starting location.
def get_number_of_steps(loc: str) -> int:
    global locations, operations

    steps = 0
    current_loc = loc

    while (not current_loc[-1] == "Z"):
        for operation in operations:

            # Case location found
            if current_loc[-1] == "Z":
                break 

            # Continue traversion
            if operation == "L":
                current_loc = locations[current_loc][0]
            else:
                current_loc = locations[current_loc][1]

            # Update amount of steps taken
            steps += 1

    return steps
    

# Program entry point
read_locations()
get_starting_locations()

# Get amount of steps of the starting loc to the first loc that ends with 'Z' 
starting_steps_to_z = [get_number_of_steps(loc) for loc in current_locations]

# Get the Least Common Multiple (LCM) of every amount in starting_steps_to_z
print(math.lcm(*starting_steps_to_z))