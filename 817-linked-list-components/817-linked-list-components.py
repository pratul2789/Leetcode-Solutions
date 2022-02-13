# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        
        tmp = head
        
        count = 0
        while tmp:
            if tmp.val in nums:
                count += 1
                while tmp.next and tmp.val in nums:
                    tmp = tmp.next
                    
            tmp = tmp.next
            
        return count