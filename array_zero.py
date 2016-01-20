#!/usr/bin/env python
# Given an array, write a function to return true if the sum of any two numbers in the array is zero

import numpy
import array

def main():
    a = [1, 66, -1, -66, 3, 4, -2, 5, 2, -4, -1]
    any_zero(a)

def any_zero(a):
    a = sorted(a)
    for i in a:
        for j in a:
            if (i + j == 0):
                print ("i %d + j %d = 0" % (i, j))

if __name__ == '__main__':
    main()

