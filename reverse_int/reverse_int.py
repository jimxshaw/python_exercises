import numpy

def reverse_int(n):
    if n < 0:
        return -1 * int(''.join(reversed(str(abs(n)))))    
    return int(''.join(reversed(str(abs(n)))))

def reverse_int_sign(n):
    # The sign method returns 1 if n is positive and -1 if negative.
    return int(''.join(reversed(str(abs(n))))) * numpy.sign(n)
