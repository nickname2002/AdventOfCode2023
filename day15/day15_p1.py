
strings_to_process = []


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


# Read input
input_file = open("input.txt", "r")

for i, line in enumerate(input_file):
    strings_to_process = line.split(",")

input_file.close()

# Process string
total_sum = 0

for s in strings_to_process:
    total_sum += hash(s.strip())

print(total_sum)
