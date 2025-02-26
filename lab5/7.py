import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])

input_text = "hello_world_example"
output_text = snake_to_camel(input_text)
print(output_text)  