class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stripped_str = [char.lower() for char in s if char.lower() in "abcdefghijklmnopqrstuvwxyz0123456789"]
        # l, r = 0, len(stripped_str)-1
        # while l <= r:
        #     if stripped_str[l] != stripped_str[r]:
        #         return False
        #     l += 1
        #     r -= 1
        
        # return True
        # s = s.lower()
        l, r = 0, len(s)-1
        while l <= r:
            while l< r and s[l].lower() not in "abcdefghijklmnopqrstuvwxyz0123456789":
                l += 1
            while l< r and s[r].lower() not in "abcdefghijklmnopqrstuvwxyz0123456789":
                r -= 1
            
            if s[l].lower()!=s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True