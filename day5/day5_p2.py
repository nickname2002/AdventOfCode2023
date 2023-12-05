
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
    seeds_and_ranges = []

    # Convert seeds to integers
    i = 0
    while i < len(seeds):
        start_of_range = int(seeds[i])
        length_of_range = int(seeds[i + 1])
        seeds_and_ranges.append((start_of_range, length_of_range))
        i += 2

    return seeds_and_ranges


# TODO: Minimize seeds list, by combining overlapping ranges
def minimize_seeds() -> None:
    pass


# TODO: Determine whether two tuples overlap
def are_overlapping() -> bool:
    pass


# Process line representing map properties
def process_map_line(line: str, map_index: int) -> None:
    global maps
    fragmented_line = line.split(" ")

    # Assign fragments of line to corresponding properties
    destination_range_start = int(fragmented_line[0])
    source_range_start = int(fragmented_line[1])
    range_length = int(fragmented_line[2])

    # Track mappings in dictionary
    maps[map_index][source_range_start] = (destination_range_start, range_length)


# Preprocessing of maps for processing stage
def build_maps() -> None:
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


# Get destination map to specific source from a specific map
def get_mapped_property(source: int, map_index: int):
    global maps 

    # Check whether the source is mapped to a destination
    for src, (dst, rng) in maps[map_index].items():
        if source >= src and source <= src + rng:
            return dst + source - src

    return source


# TODO: too in-efficient
# Find the lowest location of a specific seed
def find_lowest_location() -> int:
    current_lowest = float("inf")
    global maps

    for start_of_range, length_of_range in seeds:
        print("Initial start we're currently checking: ", start_of_range)
        for seed in range(length_of_range):
            source = seed + start_of_range
            
            for i in range(len(maps)):
                source = get_mapped_property(source, i) 
            
            if source < current_lowest:
                current_lowest = source

    return current_lowest


# Entry point of program
build_maps()
minimize_seeds()
print(find_lowest_location())
