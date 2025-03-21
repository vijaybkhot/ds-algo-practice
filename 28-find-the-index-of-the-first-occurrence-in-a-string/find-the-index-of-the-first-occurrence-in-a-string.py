class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+needle_len] == needle:
                return i
        
        return -1
        