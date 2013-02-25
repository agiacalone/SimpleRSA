#!/usr/bin/python3

# encrypt.py
# A simple RSA encryption program

import sys
import math
import cmath
from lettervalue import *

scanned_file = open('plaintext.txt').read().split()   # read in file and strip lead/trail whitespace

e = 48925           # public key
n = 88579           # public key
p = 283             # Prime #1
q = 313             # Prime #2
d = 157285          # d*e % m = 1
m = (p-1)*(q-1)     # value is 87984
final_code = []
counter = 0
#print(scanned_file)

while counter < len(scanned_file):
    # The code segment to decrypt
    phrase = scanned_file[counter]
    
    # Print out info for the user
    #print("The letters to encrypt:", phrase[0], phrase[1], phrase[2])
    
    # Get the numeric values for the letters
    val_a = lettervalue.getVal(phrase[0])
    val_b = lettervalue.getVal(phrase[1])
    val_c = lettervalue.getVal(phrase[2])
    
    # Run the scrambler
    zn = (val_a*pow(26,2)) + val_b*26 + val_c
    #print("The scrambled code is:", zn)
    
    # Now, RSA the scrambled text
    cipher = pow(zn,e) % (p*q)
    #print("The RSA cipher is:", cipher)
    
    # Put the cipher into an array for further processing
    final_code.append(cipher)
       
    # And finally, increase the counter to start the loop over again
    counter += 1

# Print out the final result for the user
print(final_code)
