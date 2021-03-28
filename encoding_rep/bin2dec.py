# -----------------------------------------------------
#                   bin2decInterval
# Converts a binary number into a floating-point decimal
# in the interval [a,b]. Each decimal number is represented
# by a string of nbits bits.
# -----------------------------------------------------
# Inputs:
#   bstr - string containing the binary number to be converted
#   a and b - [a, b] interval
#   nbits - how many bits are used in the representation of a
#   decimal number
# Output:
#   decnum - decimal number in [a,b] interval
# Usage:
#   Converting the binary string '0001' in a decimal in the
#   interval [-4,1].
#   The answer is decnum = -3.6875
#   decnum = bin2decInterval('0001',-4,1,4)
# -----------------------------------------------------
# file: bin2dec.py
# -----------------------------------------------------
def bin2decInterval(bstr, a, b, nbits):
    # Step of the representation in base 10
    delta = (b - a) / (2 ** nbits)
    # int(bstr,2) - converts a string representing a number
    # in given base to decimal.
    dnum = int(bstr,2)
    # position dnum in [a,b]
    decnum = a + delta * dnum
    return decnum

