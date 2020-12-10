import re
import pathlib

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, "input.txt")
with p.open("r", encoding="utf-8") as fs:
    input_text = fs.read()


def parse_int(input_value: str, default: int):
    try:
        return int(input_value)
    except:
        return default


input_list = str.split(input_text, "\n\n")

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
required_field_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}  # cid

valid_document_count = 0
for document in input_list:
    document = document.strip().replace("\n", " ")

    fields = str.split(document, " ")
    fields = {k: v for k, v in [str.split(field, ":") for field in fields]}
    missing = required_field_keys - set(fields.keys())

    print()
    print(document)

    if len(missing) != 0:
        print("ERROR -> invalid fields")
        continue

    if not (1920 <= parse_int(fields.get("byr"), 0) <= 2002):
        print("ERROR -> byr")
        continue

    if not (2010 <= parse_int(fields.get("iyr"), 0) <= 2020):
        print("ERROR -> iyr")
        continue

    if not (2020 <= parse_int(fields.get("eyr"), 0) <= 2030):
        print("ERROR -> eyr")
        continue

    hgt_cm = ("cm" in fields.get("hgt")) and (
        150 <= parse_int(fields.get("hgt")[:-2], 0) <= 193
    )
    hgt_in = ("in" in fields.get("hgt")) and (
        59 <= parse_int(fields.get("hgt")[:-2], 0) <= 76
    )
    if not (hgt_cm or hgt_in):
        print("ERROR -> hgt")
        continue

    if not (x := re.search(r"^#[0-9a-f]{6}$", fields.get("hcl"))):
        print("ERROR -> hcl", x)
        continue

    if not (fields.get("ecl") in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
        print("ERROR -> ecl")
        continue

    if not re.search(r"^[0-9]{9}$", fields.get("pid")):
        print("ERROR -> pid")
        continue

    valid_document_count += 1

print(valid_document_count)
