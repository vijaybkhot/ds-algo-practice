# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # num1, num2 = 0, 0
        # power1, power2 = 0, 0
        # while l1:
        #     num1 += l1.val * (10**power1)
        #     power1 += 1
        #     l1 = l1.next
        # while l2:
        #     num2 += l2.val * (10**power2)
        #     power2 += 1
        #     l2 = l2.next

        # num = num1+num2

        # if num == 0:
        #     return ListNode()

        # dummy = ListNode()
        # tail = dummy
    
        # while num:
        #     curr_val = num % 10
        #     num = num // 10
        #     tail.next = ListNode(curr_val)
        #     tail = tail.next

        # return dummy.next


        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            num = val1 + val2 + carry
            current.next = ListNode(num%10)
            carry = num // 10

            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next
        