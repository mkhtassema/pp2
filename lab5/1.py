import re

strings = [
    "a",
    "ab",
    "abb",
    "abbb",
    "b",
    "ba",
    "abbba"
]

pattern = r'ab*'

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches the pattern!")
    else:
        print(f"'{s}' does NOT match the pattern.")
