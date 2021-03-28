# -----------------------------------------------------
# Converts a string representing a gray coded number
# into a string with the corresponding binary representation
# -----------------------------------------------------
# Input:
#   gcstr     - Gray coded bit string
# Output:
#   bstr      - Binary coded bit string
# Usage:
#   bstr = gray2bin('0010')
# -----------------------------------------------------
# file: gray2bin.py
# -----------------------------------------------------
# flip a bit
def flip(c):
    return '1' if(c == '0') else '0'
# -----------------------------------------------------
def gray2bin(gcstr):
    nbits = len(gcstr)  # number of bits in gcstr
    bstr = ""           # string containing the binary
                        # representation

    # The MSBs of the binary and the Gray codes
    # are the same
    bstr = bstr + str(gcstr[0])
    # Remaining bits
    for i in range(1,nbits):
        # If current Gray bit is 0,
        # add the previous binary bit
        if gcstr[i] == '0':
            bstr = bstr + str(bstr[i-1])
        # If current Gray bit is 1, flip the
        # previous binary bit before adding
        else:
            bstr = bstr + str(flip(bstr[i-1]))
    return bstr



