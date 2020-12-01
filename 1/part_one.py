import pathlib
import math

file_location = pathlib.Path(__file__).parent
p = pathlib.Path(file_location, 'input.txt')

with p.open('r', encoding='utf-8') as fs:
    input_list = [int(x) for x in fs.readlines()]

valid_numbers = []
for i in input_list:
    for j in input_list:
        if i + j == 2020:
            valid_numbers.append(i)

if len(valid_numbers) != 2:
    raise Exception("Did not find two answers")

print("Answer:", math.prod(valid_numbers))
