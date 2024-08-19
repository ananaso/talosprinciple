#!/usr/bin/env python3

from textwrap import wrap

def clean(input_string):
	translation = str.maketrans('', '', '\n ')
	cleaned_string = input_string.translate(translation)
	return cleaned_string

def format_hex(hexstring):
	hex_arr = wrap(hexstring, 2)
	return ' '.join(hex_arr)

print("Enter/Paste your content, then normalize it with Ctrl-D: ")
inputs = []
while True:
	try:
		line = input()
	except EOFError:
		break
	inputs.append(line)
input_string = ''.join(inputs)
cleaned_string = clean(input_string)
cleaned_hexcodes = format_hex(cleaned_string)
print(cleaned_hexcodes)
