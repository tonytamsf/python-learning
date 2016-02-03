#!/usr/bin/env python

from linklistnode import linklistnode
from testy import test

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

    # find the kth element from the end, return the node
    # TODO make this more intuitive where if k < 0, then count from the end
    # test(find_kth_end(l, 3) would return the 3rd item from the end. 0 is the same as 1
    def find_kth_end(self, ll, k):
        # maintain 2 pointers and keep them k apart
        pt1 = ll
        # walk k steps, if we stop before we reach it, then return None
        for i in range(1,k+1):
            pt1 = pt1.next
            if pt1 is None:
                print("No kth element found : %d" % k)
                return None
        # walk side by side
        pt2 = ll
        while pt1:
            pt1 = pt1.next
            pt2 = pt2.next
        print("Kth element %d" % pt2.data)
        return pt2.data

    # Given a list list, see if the it's a palindrome
    # like race car
    # Return True or False
    def is_palindrome(self, l):
        ol = l
        nl = linklistnode(l.data)
        l = l.next
        while l:
            nl.insert(l.data)
            l = l.next
        print("reverse")
        nl.print_list()

        while ol:
            if ol.data != nl.data:
                return False
            ol = ol.next
            nl = nl.next
        return True
    
if __name__ == "__main__":
    l = linklistnode(3)
    for i in [5,6,3,7,9,5,6,5,6,3]:
        l.append(i)
    l.print_list()
    
    helper = linklistutils()
    helper.rm_dup(l)
    l.print_list()

    test(helper.find_kth_end(l, 100), None)
    test(helper.find_kth_end(l, 1), 6)
    test(helper.find_kth_end(l, 2), 9)
    test(helper.find_kth_end(l, 3), 7)

    pl = linklistnode('r')
    for i in ['a', 'c', 'e', 'c', 'a','r']:
        pl.append(i)
    pl.print_list()
    test(helper.is_palindrome(pl), True)

    print("2nd list")
    pl = linklistnode('r')
    for i in ['a', 'c', 'e', 'r', 'a','r']:
        pl.append(i)
    pl.print_list()
    test(helper.is_palindrome(pl), False)
    
