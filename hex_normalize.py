#!/usr/bin/env python3

def normalize(input_string):

	translation = str.maketrans('', '', '\n ')
	cleaned_string = input_string.translate(translation)
	return cleaned_string


print("Enter/Paste your content, then normalize it with Ctrl-D: ")
inputs = []
while True:
	try:
		line = input()
	except EOFError:
		break
	inputs.append(line)
input_string = ''.join(inputs)
parsed_string = normalize(input_string)
print(parsed_string)
