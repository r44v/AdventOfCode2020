import pathlib
import math

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, 'input.txt')
with p.open('r', encoding='utf-8') as fs:
    tree_map = [list(x.strip()) for x in fs.readlines()]

PATTERN_LEN = len(tree_map[0])


def get_trees(slope_y, slope_x):
    position = 0
    tree_count = 0

    for i, line in enumerate(tree_map):
        if i % slope_y != 0:
            continue
        if line[position % PATTERN_LEN] == "#":
            tree_count += 1
        position = position + slope_x
    return tree_count


slope_tree_counts = []
for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    slope_tree_counts.append(get_trees(*slope))

print(slope_tree_counts)
print(math.prod(slope_tree_counts))
