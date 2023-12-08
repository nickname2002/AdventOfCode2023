
# Traversing operations
operations = []

# Dict: (source, destination)
locations = {}
starting_location = "AAA"


# Read locations from input file.
def read_locations() -> None:
    global operations, locations, starting_location
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

        
# Get number of steps to reach "ZZZ" from the starting location.
def get_number_of_steps() -> int:
    global locations, operations, starting_location

    steps = 0
    currentLoc = starting_location

    while (not currentLoc == "ZZZ"):
        for operation in operations:

            # Case location found
            if currentLoc == "ZZZ":
                break 

            # Continue traversion
            if operation == "L":
                currentLoc = locations[currentLoc][0]
            else:
                currentLoc = locations[currentLoc][1]

            # Update amount of steps taken
            steps += 1

    return steps
    

# Program entry point
read_locations()
print(get_number_of_steps())