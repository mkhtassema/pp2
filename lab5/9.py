import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

text = "HelloWorldThisIsPython"
result = insert_spaces(text)
print(result) 