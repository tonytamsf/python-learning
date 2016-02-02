#!/usr/bin/env python

from linklistnode import linklistnode

class linklistutils():
    
    def rm_dup(self, ll):
        # time(N^2)
        pt1 = ll;
        while pt1 != None:
            data = pt1.data
            pt2 = pt1.next
            prev = pt1
            while pt2 != None:
                if pt2.data == data:
                    # remove
                    prev.next = pt2.next
                    print ("removing %d" % pt2.data)
                prev = pt2
                pt2 = pt2.next
            pt1 = pt1.next

if __name__ == "__main__":
    l = linklistnode(3)
    for i in [5,6,3,7,9,5,6,5,6,3]:
        l.append(i)
    l.print_list()
    
    helper = linklistutils()
    helper.rm_dup(l)
    l.print_list()

