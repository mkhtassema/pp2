import re

pattern = r'ab{2,3}'

def match_string(s):
    if re.fullmatch(pattern, s):
        return "Match found!"
    else:
        return "No match."

test_strings = ["abb", "abbb", "abbbb", "a", "b", "aabb"]
for test in test_strings:
    print(f"Testing '{test}': {match_string(test)}")
