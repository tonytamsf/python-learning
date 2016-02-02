#!/usr/bin/env python

import sys
from testy import test

# reverse a string
def reverse(s):
    l = len(s)
    ns = ''
    for i in range(l-1, -1, -1):
        ns += s[i]
    return ns

if __name__ == '__main__':
    print test(reverse("take this"), 'siht ekat')
