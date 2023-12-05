
# Seeds
seeds: list = []

# Maps
maps = [
    {},     # seed-to-soil
    {},     # soil-to-fertilizer
    {},     # fertilizer-to-water
    {},     # water-to-light
    {},     # light-to-temperature
    {},     # temperature-to-humidity
    {}      # humidity-to-location
]


# Read seeds from input file
def read_seeds(line: str) -> list:
    seeds = line.split(": ")[1].split(" ")

    # Convert seeds to integers
    for i, seed in enumerate(seeds):
        seeds[i] = int(seed)

    return seeds


# Process line representing map properties
def process_map_line(line: str, map_index: int):
    global maps
    fragmented_line = line.split(" ")

    # Assign fragments of line to corresponding properties
    destination_range_start = int(fragmented_line[0])
    source_range_start = int(fragmented_line[1])
    range_length = int(fragmented_line[2])

    # Track mappings in dictionary 
    for i in range(range_length):
        maps[map_index][destination_range_start + i] = source_range_start + i


# Preprocessing of maps for processing stage
def build_maps():
    global seeds

    # Open in put file
    file = open("day5/input.txt", "r")

    map_index: int = 0
    for i, line in enumerate(file):

        # Process empty line
        if line in ["\n", "\r\n"] and i == 1:
            continue
        elif line in ["\n", "\r\n"]:
            map_index += 1

        # Read seeds
        if line.__contains__("seeds"):
            seeds = read_seeds(line)
            # print("Reading seeds: ", seeds)
            continue

        # Detect start of new map reading 
        if line[0].isdigit():
            # print(map_index, ": Processing map line: ", line)
            process_map_line(line, map_index)
            
    file.close()


# Entry point of program
build_maps()

