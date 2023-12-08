
# Traversing operations
operations = ""

# Dict: (source, destination)
locations = {}


# Read locations from input file.
def read_locations() -> None:
    global operations, locations
    input_file = open("day8/input.txt", "r")

    for i, line in enumerate(input_file):

        # Read operations
        if i == 0:
            operations = [*line]

        # Read locations
        if i >= 2:
            # TODO: Read locations
            pass

        

    