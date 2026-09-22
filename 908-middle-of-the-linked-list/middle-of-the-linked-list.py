# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        current = head
        return_val = ListNode()

        while current is not None:
            count += 1
            current = current.next
        
        mid = count // 2

        current = head
        
        for _ in range(mid):
            current = current.next
            
        return current