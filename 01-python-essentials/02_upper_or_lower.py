#!/usr/bin/env python

def upper_or_lower(str):
    if str.isupper():
        print(f"{str} is uppercase.")
    elif str.islower():
        print(f"{str} is lowercase.")
    else:
        print(f"{str} is neither uppercase nor lowercase.")

upper_or_lower('HARSHVARDHAN')
upper_or_lower('harshvardhan')
upper_or_lower('Harshvardhan')
