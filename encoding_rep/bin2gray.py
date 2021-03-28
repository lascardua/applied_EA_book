# -----------------------------------------------------
# Converts a binary coded number into its Gray code
# representation
# -----------------------------------------------------
# Input:
#   bstr      - Binary coded bit string
# Output:
#   gcstr     - Gray coded bit string
# Usage:
#   gcstr = bin2gray('0011')
# -----------------------------------------------------
# file: bin2gray.py
# -----------------------------------------------------
def bin2gray(bstr):
    nbits = len(bstr)   # number of bits in bstr
    gcstr = ""          # string containing the binary
                        # representation

    # The MSBs of the binary and the Gray codes
    # are the same
    gcstr = gcstr + str(bstr[0])
    # The next bit  is computed as the XOR of the
    # previous  and current binary bits
    for i in range(1,nbits):
        gcstr = gcstr + str(int(bstr[i - 1]) ^ int(bstr[i]))

    return gcstr


