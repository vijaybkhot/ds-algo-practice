# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # count len of list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        power = length-1

        num = 0
        curr = head
        for i in range(length):
            curr_bit = curr.val
            curr = curr.next
            num += 1 << power if curr_bit == 1 else 0
            power -= 1
        
        return num

        