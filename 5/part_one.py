import pathlib

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, "input.txt")
with p.open("r", encoding="utf-8") as fs:
    boarding_passes = [x.strip() for x in fs.readlines()]

seat_ids = []


def get_change(char, option_min, option_max, rest):
    rest = rest / 2
    if char == "F" or char == "L":
        return option_min, option_max - rest, rest
    if char == "B" or char == "R":
        return option_min + rest, option_max, rest


def get_position(total, options):
    option_min = 0
    option_max = total - 1
    rest = total
    for char in options:
        option_min, option_max, rest = get_change(char, option_min, option_max, rest)
    return option_min


seat_ids = []
for boarding_pas in boarding_passes:
    row = get_position(128, boarding_pas[:7])
    col = get_position(8, boarding_pas[7:])

    seat_ids.append(int(row * 8 + col))

print(max(seat_ids))