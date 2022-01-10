# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:
            return head
        
        def incrementFast(fast,k):
            i = 1
            while fast and i < k:
                fast = fast.next
                i = i + 1
                
            if fast == None and i <= k:
                return None
            
            return fast
        
        
        pdum = None
        cdum = None
        ctail = None
        ptail = None
        pptail = None
        
        slow,fast,tmp = head,head,head
        while True:
            fast = incrementFast(fast,k)
            if fast == None:
                ptail.next = slow
                return pdum

            fin = fast.next
            while slow != fin:
                if cdum == None:
                    cdum = slow
                    slow = slow.next
                    ctail = cdum
                    cdum.next = None
                else:
                    tmp = slow.next
                    slow.next = cdum
                    cdum = slow
                    slow = tmp
            if ptail == None:
                ptail = ctail
                pdum = cdum
            else:
                ptail.next = cdum
                ptail = ctail
            #pdum = cdum
            cdum = None
            
            slow,fast,tmp = fin,fin,fin