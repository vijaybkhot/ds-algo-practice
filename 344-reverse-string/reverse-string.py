class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # left_p = 0
        # right_p = len(s)-1
        # while right_p > left_p:
        #     s[left_p], s[right_p] = s[right_p], s[left_p]
        #     left_p += 1
        #     right_p -= 1
        
        # return s

        # Simpler python syntax to reverse in place
        s[:] = s[::-1]
        