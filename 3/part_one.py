import pathlib

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, 'input.txt')
with p.open('r', encoding='utf-8') as fs:
    tree_map = [list(x.strip()) for x in fs.readlines()]

SLOPE_X = 3
SLOPE_Y = 1
PATTERN_LEN = len(tree_map[0])

position = 0, 0
tree_count = 0

# skip first so output matches example
print(str.join('', tree_map[0]))
for line in tree_map[1:]:
    position = position[0] + SLOPE_Y, position[1] + SLOPE_X
    if line[position[1] % PATTERN_LEN] == "#":
        tree_count += 1
        line[position[1] % PATTERN_LEN] = 'X'
    else:
        line[position[1] % PATTERN_LEN] = 'O'
    print(str.join('', line))

print(tree_count)
