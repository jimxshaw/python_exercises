from functools import reduce

def reverse_string_reversed(input):
    return ''.join(reversed(input))

def reverse_string_slice(input):
    return input[::-1]

def reverse_string_loop(input):
    reversed_string = ''
    for char in input:
        reversed_string = char + reversed_string
    return reversed_string

def reverse_string_reduce(input):
    # Param1: lambda function adds the character to the existing accumulator for each character.
    # Param2: item to be iterated over.
    # Param3: accumulator is set to an initial value, which is a blank string.
    return reduce(lambda accumulator, character: character + accumulator, input, '')