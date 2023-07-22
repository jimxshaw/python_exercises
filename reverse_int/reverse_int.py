def reverse_int(input):
    if input < 0:
        return -1 * int(''.join(reversed(str(abs(input)))))
    
    return int(''.join(reversed(str(abs(input)))))
