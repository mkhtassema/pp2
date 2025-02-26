import re

def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

text = "camelCaseToSnakeCase"
result = camel_to_snake(text)
print(result) 