#!/usr/bin/env python3

def bin_to_dec_no_error(binary_array):
    decimal = 0
    for index, current_bit in enumerate(reversed(binary_array)):
        if current_bit == 1 or current_bit == True:
            decimal += 2**(index)

def bin_to_dec(binary_array):

    if len(binary_array) != 4:
        print("Error: Wrong length of binary_array. It needs to be 4. For example: [0, 0, 1, 1]")
        return -1

    decimal = 0
    for index, current_bit in enumerate(reversed(binary_array)):

        if current_bit == 1: 
            decimal += 2**(index)
        elif current_bit != 0:
            print("Error: binary_array[{}] with value of: \"{}\" is not a boolean. Like: 0, 1, True or False "
                    .format(str(index), str(current_bit)))
            return -1

    return decimal

assert bin_to_dec([1,1,0,0]) == 12
assert bin_to_dec([True,True,False,False]) == 12
assert bin_to_dec([0,1,0,1]) == 5
assert bin_to_dec([1,1,1,0]) == 14
assert bin_to_dec([0,1,1,1]) == 7
assert bin_to_dec([0,2,1,1]) == -1 # expects errormessage
assert bin_to_dec([0,"a",1,1]) == -1 # expects errormessage
assert bin_to_dec([0,0,1,1,1]) == -1 # expects errormessage
assert bin_to_dec([1,1,1]) == -1 # expects errormessage
