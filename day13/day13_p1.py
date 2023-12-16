

def match_detected(ls: list) -> (int, int):
    for i in range(len(ls)):

        # Check for reflection with border length 1
        fst = ls[0 : i]
        fst.reverse()
        snd = ls[i + 1 : len(ls)]

        if fst[0:len(snd)] == snd and snd != []:
            return (i, 1)

        # Check for reflection with border lenth 2
        fst = ls[0 : i]
        fst.reverse()
        snd = ls[i + 2 : len(ls)]

        if fst[0:len(snd)] == snd and snd != []:
            return(i, 2)

    return None    


def process_pattern(pattern: list):

    # Check for col pattern
    row_pattern = None
    for row in pattern:
        match = match_detected(row)
        if match == None and row_pattern != None:
            row_pattern = None
            break
        row_pattern = match

    if row_pattern != None:
        return (row_pattern[0], 
                len(pattern[0]) - row_pattern[0] - row_pattern[1])

    # Check rows pattern
    col_pattern = None
    for i in range(len(pattern[0])):
        col = [row[i] for row in pattern]
        match = match_detected(col)
        if col == None and col_pattern != None:
            col_pattern = None
            break
        col_pattern = match

    if col_pattern != None:
        return (col_pattern[0] - 1, 
                len(pattern) - col_pattern[0] - col_pattern[1])


def visualize_pattern(pattern: list) -> None:
    print("====================")

    for row in pattern:
        print(row)
    
    print("====================")


# Entry point
input_file = open("day13/input.txt", "r")
pattern_buffer = []

for line in input_file:
    
    # Case empty line - Process pattern 
    if line == "\n":
        print(process_pattern(pattern_buffer))
        pattern_buffer.clear()
        continue

    # Case non-empty line - Fill pattern buffer
    pattern_buffer.append([*line.strip()])

print(process_pattern(pattern_buffer))
input_file.close()