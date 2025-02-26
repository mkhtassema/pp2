import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text = "Hello World, this is a Test String with Patterns."
result = find_sequences(text)
print("Sequences found:", result)
