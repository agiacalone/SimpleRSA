#!/usr/bin/python3

# decrypt.py
# A simple RSA decryption program

import sys
import math
import cmath
from lettervalue import *

scanned_file = open('code.txt').read().split()   # read in file and strip lead/trail whitespace

e = 48925           # public key
n = 88579           # public key
p = 283             # Prime #1
q = 313             # Prime #2
d = 157285          # d*e % m = 1
m = (p-1)*(q-1)     # value is 87984
final_array = []
counter = 0

while counter < len(scanned_file):
    # The code segment to decrypt
    code = int(scanned_file[counter])
    
    # Print out for the user
    #print("The ciphered number is:", code)
    
    # Decipher the encrypted text
    decipher = pow(code,d) % (p*q)
    #print("The unciphered scramble is:", decipher)
    
    # Unscramble the cipher
    mod_a = int (decipher*pow((1/26),2) % 26)
    mod_b = int (decipher/26 % 26)
    mod_c = int (decipher % 26)
    #print("The letter values:", mod_a, mod_b, mod_c)
    
    # Get the letters based on the table
    lett_a = lettervalue.getLett(mod_a)
    lett_b = lettervalue.getLett(mod_b)
    lett_c = lettervalue.getLett(mod_c)
    #print("The unscrambled cipher is:", lett_a, lett_b, lett_c)
    
    # Put the letters into an array for further processing
    final_array.append(lett_a + lett_b + lett_c)
    
    # And finally, increase the counter to start the loop over again
    counter += 1

# Print out the final result for the user
print(final_array)
