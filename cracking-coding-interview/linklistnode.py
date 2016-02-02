#!/usr/bin/env python

from testy import test

class linklistnode:
    def __init__(self, d):
        self.data = d
        self.next = None
        
    def insert(self, d):
        n = linklistnode(self.data)
        self.data = d
        n.next = self.next
        self.next = n

    def append(self, d):
        n = self
        new_node = linklistnode(d)
        while n:
            if not n.next:
                n.next = new_node
                break
            else:
                pass
            n = n.next

    def print_list(self):
        n = self;
        while n:
            print(n.data)
            n = n.next

if __name__ == "__main__":
    l = linklistnode(154)
    test(l.data, 154)
    l.append(3)
    test(l.data, 154)
    test(l.next.data, 3)
    
    l.insert(7)
    print (l.data)
    test(l.data, 7)
    test(l.next.data, 154)
    test(l.next.next.data, 3)
    test(l.next.next.next, None)
    
    l.append(300)
    l.print_list()

