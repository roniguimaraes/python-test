#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Roni
#
# Created:     23/11/2024
# Copyright:   (c) Roni 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

#Enter two integer numbers
    f_number = int(input("Enter first number"))
    s_number = int(input("Enter second number"))

#Perform arithmetic operations with them
    add = f_number + s_number
    sub = f_number - s_number
    mul = f_number * s_number
    div = f_number // s_number
    flo = f_number / s_number
    mod = f_number % s_number

#Print operations
    print(add)
    print(sub)
    print(mul)
    print(div)
    print(flo)
    print(mod)

"""
About string manipulation

I might have seen it at some point
but I dont remember how to find a str length
or to convert it to upper or lowercase
I could google it
but since the idea is to test my knowledge...
"""

if __name__ == '__main__':
    main()
