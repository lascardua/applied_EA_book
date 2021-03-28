# -----------------------------------------------------
#                gray2decInterval
# Converts a Gray number into a decimal in  [a,b].
# Each decimal number is represented by a string of
# nbits_dv bits.
# -----------------------------------------------------
# Inputs:
#   gcstr       - string containing the gray coded number
#   a and b     - [a, b] decimal interval
#   nbits_dv    - how many bits are used in the representation
#                 of a decimal number
# Output:
#   decnum      - decimal number in [a,b] interval
# Usage:
#   Converting the binary string '0001' in a decimal in
#   the interval [-4,1].
#   decnum = gray2decInterval('0001',-4,1,4)
#   The answer is decnum = -3.6875
# -----------------------------------------------------
# file: gray2dec.py
# -----------------------------------------------------
from encoding_rep.gray2bin import gray2bin
# -----------------------------------------------------

def gray2decInterval(gcstr, a, b, nbits_dv):
    # Step of the representation in base 10
    delta = (b - a) / (2 ** nbits_dv)
    # converts a gray coded string representing a number in given base to decimal.
    dnum =gray2dec(gcstr)
    # position dnum in [a,b]
    decnum = a + delta * dnum
    return decnum

def gray2dec(gcstr):
    bstr =  gray2bin(gcstr)
    dnum = int(bstr, 2)
    return dnum


