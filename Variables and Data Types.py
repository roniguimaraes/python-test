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

#Declare variables and assign values
    name = "Roni"
    age = 22
    is_student = True

#Print the variables
    print(name)
    print(age)
    print(is_student)

#Convert the variables
    cnv_age = str (age)
    cnv_is_student = int (is_student)

#Print converted values
    print("{} is {}yo".format(name, cnv_age))
    print(cnv_is_student)

if __name__ == '__main__':
    main()
