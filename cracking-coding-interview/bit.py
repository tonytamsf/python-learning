#!/usr/bin/env python

from testy import test

class bit:
    # get bit
    # getbit(8, 3) == 1
    # getbit(8, 0) == 0
    def getbit(self, num, i):
        return (num & (1 << i)) >> i

    def setbit(self, num, i):
        return (num | (1 << i))

    def clearbit(self, num, i):
        return num & ~(1 << i)

    def insertbits(self, N, M, i, j):
        allones = (2**32)-1
        n1 = allones << j + 1
        n2 = (1 << (i)) - 1
        #print("{0:b}".format(n1))
        #print("{0:b}".format(n2))
        n3 = n1 | n2
        #print("n3 {0:b}".format(n3))
        #print("M << i {0:b}".format(M << i))
        #print("N {0:b}".format(N))
        #print("n3 & N {0:b}".format(n3 & N))
        #print("{0:b}".format(n3 & N & (M << i)))
        final = (n3 & N | (M << i))
        print("{0:b}".format(final))
        return (n3 & N | (M << i))
    
if __name__ == '__main__':
    b = bit()
    test(b.getbit(8, 3), 1)
    test(b.getbit(8, 0), 0)
    
    test(b.setbit(8, 0), 9)
    test(b.setbit(8, 1), 10)
    test(b.setbit(1, 1), 3)
    test(b.setbit(1, 0), 1)

    test(b.clearbit(8, 3), 0)
    test(b.clearbit(8, 0), 8)

    test(b.insertbits(0b10000000000, 0b0000000010011, 2, 6), 0b10001001100)
