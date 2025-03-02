class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_p = 0
        right_p = len(s)-1

        while right_p > left_p:
            if not s[left_p].isalnum() or not s[right_p].isalnum():
                if not s[left_p].isalnum():
                    left_p += 1
                if not s[right_p].isalnum():
                    right_p -= 1
                continue
            if ord(s[left_p].lower()) !=  ord(s[right_p].lower()):
                return False
            left_p += 1
            right_p -= 1
        
        return True
                
        