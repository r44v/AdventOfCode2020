import pathlib
import math

file_location = pathlib.Path(__file__).parent
p = pathlib.Path(file_location, 'input.txt')

with p.open('r', encoding='utf-8') as fs:
    input_list = [int(x) for x in fs.readlines()]


def get_valid_numbers():
    valid_numbers = []
    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i + j + k == 2020:
                    valid_numbers.append(i)
                    valid_numbers.append(j)
                    valid_numbers.append(k)
                    return valid_numbers


valid_numbers = get_valid_numbers()

print("Numbers:", valid_numbers)
print("Answer:", math.prod(valid_numbers))
