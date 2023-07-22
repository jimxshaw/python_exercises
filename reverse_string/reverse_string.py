def reverse_string_slice(input):
    return input[::-1]

def reverse_string_loop(input):
    reversed_string = ""
    for char in input:
        reversed_string = char + reversed_string
    return reversed_string
