# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def get_gcd(num1, num2):
            gcd = min(num1, num2)
            while gcd > 0 and num1%gcd or num2%gcd:
                gcd -= 1
            
            return gcd
        
        dummy = ListNode()
        dummy.next = head
        curr = head.next
        prev = head
        while curr:
            num1, num2 = prev.val, curr.val
            gcd = get_gcd(num1, num2)
            gcd_node = ListNode(val=gcd)
            prev.next = gcd_node
            gcd_node.next = curr
            prev = curr
            curr = curr.next

        return dummy.next
        