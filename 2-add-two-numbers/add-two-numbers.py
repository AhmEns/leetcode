# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        num1 = 0
        num2 = 0
        multiplier = 1

        while l1:
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next

        multiplier = 1
        while l2:   
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next

        total = num1 + num2

        if total == 0:
            return ListNode(0)  
        elif total < 0:
            return None
        else:
            head = None
            current = None

            while total > 0:
                digit = total % 10
                total //= 10

                new_node = ListNode(digit)

                if head is None:
                    head = new_node
                    current = new_node
                else:
                    current.next = new_node
                    current = current.next

            return head