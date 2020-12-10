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


def get_seat_id(boarding_pas):
    row = get_position(128, boarding_pas[:7])
    col = get_position(8, boarding_pas[7:])
    return int(row * 8 + col)


seat_ids = list(range(get_seat_id("BBBBBBBRRR") + 1))
for boarding_pas in boarding_passes:
    seat_ids.pop(seat_ids.index(get_seat_id(boarding_pas)))

for open_seat in seat_ids:
    if open_seat + 1 in seat_ids or open_seat - 1 in seat_ids:
        continue
    print(open_seat)
