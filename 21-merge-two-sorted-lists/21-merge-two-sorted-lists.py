# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3  = ListNode('#')
        tmp = l3
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        
        while l1:
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next
        while l2:
            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next
        return l3.next
            