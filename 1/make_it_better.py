import pathlib
import math

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, 'input.txt')
with p.open('r', encoding='utf-8') as fs:
    input_list = [int(x) for x in fs.readlines()]

SUM_VALUE = 2020
TERMS_LEN = 2


def get_(terms):
    if len(terms) < TERMS_LEN:
        for i in input_list:
            has_answer, answer = get_(terms + [i])
            if has_answer:
                return has_answer, answer
        return False, None
    else:
        term_sum = sum(terms)
        if term_sum == SUM_VALUE:
            return True, terms
        else:
            return False, None

valid_numbers = get_([])[1]

print("Numbers:", valid_numbers)
print("Answer:", math.prod(valid_numbers))
