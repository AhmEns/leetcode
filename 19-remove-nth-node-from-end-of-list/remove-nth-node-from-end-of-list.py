# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        len = 0
        temp = head

        while temp is not None:
            len += 1
            temp = temp.next
        
        curr = head
        
        if len == n:
            return head.next
        
        for _ in range(len - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head