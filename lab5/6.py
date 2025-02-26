def replace_with_colon(text):
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')

input_text = "Hello, world. How are you?"
output_text = replace_with_colon(input_text)
print(output_text)