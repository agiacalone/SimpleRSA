#!/usr/bin/python3

# lettervalue.py

class lettervalue:
    # Define the alphabet: a=0, b=1, c=2, and so on...
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # This method will return the value when you have the letter
    def getVal(letter):
        for x in range(0,26):
            if letter  == lettervalue.alphabet[x]:
                return x
            else:
                x += 1
    
    # This method will return the letter when you have the value
    def getLett(value):
        return lettervalue.alphabet[value]
