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
        allones = (2**32)-1    # 111111111
        n1 = allones << j + 1  # 111100000
        n2 = (1 << (i)) - 1    # 000000011 
        n3 = n1 | n2           # 111100011
        final = (n3 & N | (M << i)) # 111100011 & N masks, then shift M into place and OR it
        return final
    
    # number of bits to shift from A to B
    def num_bits_to_shift(self, a, b):
        num = 0
        # bit by bit from the right.  Calculate the difference
        while a != 0:
            if self.getbit(a, 0) ^ self.getbit(b,0) == 1:
                num += 1
            a = a >> 1
            b = b >> 1
        return num
    
        return -1

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

    test(b.num_bits_to_shift(0b11101, 0b01111), 2)
