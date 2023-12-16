
strings_to_process = []
hash_map = {}


# Get the hash of a string
def hash(s: str) -> int:
    current = 0

    # Process every char in s
    for c in s:
        ascii_code = ord(c)
        current += ascii_code
        current *= 17
        current = current % 256

    return current


# Remove element from hash map
def remove_element(s: str) -> None:
    global hash_map

    # Get string to search for
    fragments = s.split("-")
    string_to_search = fragments[0]
    hash_of_elem = hash(string_to_search)

    # Remove element
    if hash_of_elem in hash_map.keys():
        for string, id in hash_map[hash_of_elem]:
            if string == string_to_search:
                hash_map[hash_of_elem].remove((string, id))
                break


# Add element to hash map
def add_element(s: str) -> None:
    global hash_map

    # Prepare string
    fragments = s.split("=")
    hash_of_elem = hash(fragments[0])
    tuple_to_add = (fragments[0], fragments[1])

    # Add element
    if hash_of_elem in hash_map.keys():

        for i, t in enumerate(hash_map[hash_of_elem]):
            if t[0] == fragments[0]:
                hash_map[hash_of_elem][i] = tuple_to_add
                return

        hash_map[hash_of_elem].append(tuple_to_add)
    else:
        hash_map[hash_of_elem] = [tuple_to_add]


# Read input
input_file = open("input.txt", "r")

for i, line in enumerate(input_file):
    strings_to_process = line.split(",")

input_file.close()

# Process strings
for s in strings_to_process:
    if s.__contains__("="):
        add_element(s)
    else:
        remove_element(s)

# Remove empty keys
hash_map = { key:val for key, val in hash_map.items() if val != []}

# Calculate sum
total_sum = 0

for box in hash_map.keys():
    for slot, (b, f) in enumerate(hash_map[box]):
        focal_length = int(f.strip())
        total_sum += (box + 1) * (slot + 1) * focal_length

print(total_sum)
