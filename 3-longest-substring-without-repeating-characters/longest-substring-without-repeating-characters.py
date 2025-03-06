class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Using dynamic sliding window and a hash set to track the length of longest substring
        output = 0
        left = 0
        unique_set = set()

        for right in range(len(s)):
            if s[right] in unique_set:
                while True:
                    unique_set.remove(s[left])
                    left += 1
                    if s[right] not in unique_set:
                        break
            unique_set.add(s[right])
            if len(unique_set) > output:
                output = len(unique_set)
        
        return output