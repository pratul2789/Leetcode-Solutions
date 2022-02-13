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
        
        
        if not head:
            return 0
        nums = set(nums)
        vis = set()
        
        def dfs(node):
            if node in vis:
                return
            
            vis.add(node)
            
            if node.next and node.next.val in nums:
                dfs(node.next)
            
            return
        
        
        tmp = head
        count = 0
        while tmp:
            if tmp.val in nums and tmp not in vis:
                dfs(tmp)
                count += 1
                
            tmp = tmp.next
            
        
        
        return count