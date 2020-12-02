import pathlib

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, 'input.txt')
with p.open('r', encoding='utf-8') as fs:
    input_list = [x.strip() for x in fs.readlines()]


def check_if_valid(line: str) -> bool:
    condition, password = str.split(line, ': ')
    condition, character = str.split(condition, ' ')
    condition_a, condition_b = str.split(condition, '-')
    return int(condition_a) <= password.count(character) <= int(condition_b)


total_matching_passwords = sum([1 for x in input_list if check_if_valid(x)])
print(total_matching_passwords)
