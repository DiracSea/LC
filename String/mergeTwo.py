# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, a, b):
        if a and b: 
            if a.val > b.val: 
                a, b = b, a 
            a.next = self.mergeTwoLists(a.next, b) 
        return a or b 

    def mergeTwoLists1(self, a, b):
        copy = cur = ListNode(0) 
        while a and b: 
            if a.val < b.val: 
                cur.next = a 
                a = a.next 
            else: 
                cur.next = b 
                b = b.next 
            cur = cur.next
        cur.next = a or b 
        return copy.next  