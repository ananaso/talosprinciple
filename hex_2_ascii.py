#!/usr/bin/env python3

def hex_2_ascii(hexstring):
    hexvals = hexstring.split()
    translated = ''
    for index in range(0, len(hexvals)):
        letter = chr(int(hexvals[index], 16))
        translated = translated + letter
    return translated


hexstring = input("Hexstring: ")
asciistring = hex_2_ascii(hexstring)
print(asciistring)
