import re

def match_pattern(text):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, text))

input_text = "acb"
print(match_pattern(input_text))  

input_text = "a123b"
print(match_pattern(input_text))  

input_text = "b123a"
print(match_pattern(input_text))  
