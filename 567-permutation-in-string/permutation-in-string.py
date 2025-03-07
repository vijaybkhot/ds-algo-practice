class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        # using fixed size sliding window
        # Create frequency map of s1 to account for all permutations of s1
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        # Create a starting widow in s2 and check 
        left = 0
        window_map = {}
        for i in range(len(s1)):
            window_map[s2[i]] = window_map.get(s2[i], 0) + 1
        
        if s1_map == window_map:
            return True
        
        for right in range(len(s1), len(s2)):
            # Remove the leftmost element from window
            window_map[s2[left]] = window_map.get(s2[left]) - 1
            if window_map[s2[left]] == 0:
                del window_map[s2[left]]
            # Add the new right element
            window_map[s2[right]] = window_map.get(s2[right], 0) + 1
            if s1_map == window_map:
                return True
            left += 1
        
        return False


        