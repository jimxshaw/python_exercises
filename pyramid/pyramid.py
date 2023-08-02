def pyramid(n):
    output = ''
    for i in range(n):
        output += ' ' * (n - i - 1) + '#' * (2 * i + 1) + ' ' * (n - i - 1) + "\n"
    return output.rstrip()  # Remove the trailing newline.
