def palindrome_slice(input):
    return input[::-1] == input

def palindrome_reversed(input):
    return ''.join(reversed(input)) == input

def palindrome_loop(input):
    front = 0
    back = len(input) - 1

    while front < back:
        if input[front] != input[back]:
            return False
        front += 1
        back -= 1

    return True
