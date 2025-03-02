class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        def isPalindrome(sub_s, left, right):
            while left < right:
                if sub_s[left] != sub_s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left_p, right_p = 0, len(s)-1
        while left_p < right_p:
            if s[left_p] != s[right_p]:
               return isPalindrome(s, left_p+1, right_p) or isPalindrome(s, left_p, right_p-1)
            left_p += 1
            right_p -= 1
        
        return True