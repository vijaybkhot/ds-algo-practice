# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not nums:
            return head

        dummy = ListNode()
        dummy.next = head

        curr = dummy.next
        prev = dummy

        nums = set(nums)
        while curr:
            if curr.val in nums:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next

            