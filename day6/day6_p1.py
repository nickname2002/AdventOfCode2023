
time = []                       # In ms
distance = []                   # In mm
amount_of_winning_times = []   


# Read time from line
def read_time(line) -> list:
    times: list = line.split(": ")[1].split(" ")
    
    # Remove spaces from times list
    while times.__contains__(""):
        times.remove("")

    # Convert entries in list to int
    for i in range(len(times)):
        times[i] = int(times[i])

    return times


# Read distances from line
def read_distance(line):
    distances: list = line.split(": ")[1].split(" ")
    
    # Remove spaces from times list
    while distances.__contains__(""):
        distances.remove("")

    # Convert entries in list to int
    for i in range(len(distances)):
        distances[i] = int(distances[i])

    return distances


# Fill time and distance lists
def read_input():
    global time, distance
    input_file = open("day6/input.txt", "r")

    for i, line in enumerate(input_file):
        if i == 0:
            time = read_time(line)
            continue

        distance = read_distance(line)


# Calculate the distance after holding the button for `ms_held` seconds
def calc_distance(ms_held: int, total_race_ms) -> int:
    remaining_seconds = total_race_ms - ms_held
    return remaining_seconds * ms_held


# Program entry point
read_input()

# Calculate ms_held to win per race
for race_id, ms in enumerate(time):
    
    current_record_dist = distance[race_id]
    winning_holding_times_for_race = []

    # Calculate all the times
    for holding_time in range(ms):
        dist = calc_distance(holding_time, ms)

        if dist > current_record_dist:
            winning_holding_times_for_race.append(holding_time)

    amount_of_winning_times.append(len(winning_holding_times_for_race))

product = 1
for amount in amount_of_winning_times:
    product *= amount
print(product)