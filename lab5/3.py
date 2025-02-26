import re

pattern = r'[a-z]+(?:_[a-z]+)*'

def match_string(s):
    if re.fullmatch(pattern, s):
        return "Match found!"
    else:
        return "No match."

test_strings = ["hello_world", "hello_world_test", "helloWorld", "hello__world", "hello", "hello_"]
for test in test_strings:
    print(f"Testing '{test}': {match_string(test)}")
