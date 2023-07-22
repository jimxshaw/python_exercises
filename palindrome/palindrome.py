def palindrome_slice(input):
    return input[::-1] == input

def palindrome_reversed(input):
    return ''.join(reversed(input)) == input
