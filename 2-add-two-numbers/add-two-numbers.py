# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        sumTotal = 0
        carry = 0 

        while l1 or l2 or carry:
            l1_temp = l1.val if l1 else 0
            l2_temp = l2.val if l2 else 0
            sumTotal = l1_temp + l2_temp + carry
            carry = sumTotal // 10 
            current.next = ListNode(sumTotal % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next