
from encoding_rep.gray2bin import gray2bin
from encoding_rep.bin2gray import bin2gray
from encoding_rep.gray2dec import gray2decInterval

from encoding_rep.dec2bin import dec2bin


bstr = '0011'
gcstr = bin2gray(bstr)
print("bin2gray {} -> {}".format(bstr,gcstr))

gcstr = '0010'
bstr = gray2bin(gcstr)
print("gray2bin {} -> {}".format(gcstr,bstr))

gcstr = '0001'
a = -4
b = 1
nbits_dv = 4
decnum = gray2decInterval(gcstr,a,b,nbits_dv)
print("gray2decInterval {} -> {}".format(gcstr,decnum))


dec = 32
bstr = dec2bin(dec)
gcstr = bin2gray(bstr)
print("dec2gray {} -> {}".format(dec,gcstr))