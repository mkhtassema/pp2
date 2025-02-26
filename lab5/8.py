import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

text = "HelloWorldThisIsPython"
result = split_at_uppercase(text)
print(result)