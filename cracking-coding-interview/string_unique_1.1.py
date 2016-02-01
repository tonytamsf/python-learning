#!/usr/bin/env python

from testy import test

# return true if string has all unique characters
def string_unique(s):
    h = {}
    for c in s:
        if c in h:
            return False
        else:
            h[c] = 1
    return True

if __name__ == '__main__':
    print test(string_unique('tony tam is not unique'), False)
    print test(string_unique('tony am'), True)
