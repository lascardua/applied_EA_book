# -----------------------------------------------------
#                dec2bin
# Converts a decimal number in its binary representation
# -----------------------------------------------------
# Inputs:
#   dec        - decimal number
# Output:
#   bstr       - binary string
# Usage:
#   Converting 58 into binary
#   bstr = dec2bin(58)
# -----------------------------------------------------
# file: dec2bin.py
# -----------------------------------------------------
def dec2bin(dec):
    return bin(dec).replace("0b", "")