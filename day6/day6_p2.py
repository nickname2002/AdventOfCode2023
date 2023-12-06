
time = 0                       # In ms
record = 0                   # In mm


# Read time from line
def read_time(line) -> int:
    times: list = line.split(": ")[1].split(" ")
    read_time = ""

    # Remove spaces from times list
    while times.__contains__(""):
        times.remove("")

    # Concatenate all elements in times
    times.reverse()
    for i in times:
        read_time = i + read_time

    return int(read_time)


# Read distances from line
def read_distance(line):
    distances: list = line.split(": ")[1].split(" ")
    read_dist = ""
    
    # Remove spaces from times list
    while distances.__contains__(""):
        distances.remove("")

    # Concatenate all elements in distance
    distances.reverse()
    for i in distances:
        read_dist = i + read_dist
        
    return int(read_dist)


# Fill time and distance lists
def read_input():
    global time, record
    input_file = open("day6/input.txt", "r")

    for i, line in enumerate(input_file):
        if i == 0:
            time = read_time(line)
            continue

        record = read_distance(line)


# Calculate the distance after holding the button for `ms_held` seconds
def calc_distance(ms_held: int, total_race_ms) -> int:
    remaining_seconds = total_race_ms - ms_held
    return remaining_seconds * ms_held


# Program entry point
read_input()

# Calculate ms_held to win per race
winning_holding_times_for_race = []

# Calculate all the times
for holding_time in range(time):
    dist = calc_distance(holding_time, time)

    if dist > record:
        winning_holding_times_for_race.append(holding_time)

print(len(winning_holding_times_for_race))
