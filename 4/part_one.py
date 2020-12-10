import pathlib

# Get current file location
file_location = pathlib.Path(__file__).parent

# Get input data
p = pathlib.Path(file_location, "text_input.txt")
with p.open("r", encoding="utf-8") as fs:
    input_text = fs.read()

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
    field_keys = set([str.split(field, ":")[0] for field in fields])

    missing = required_field_keys - field_keys
    if len(missing) == 0:
        valid_document_count += 1

print(valid_document_count)
