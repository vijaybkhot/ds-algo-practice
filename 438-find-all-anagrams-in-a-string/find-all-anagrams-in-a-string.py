class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        k = len(p)
        output = []
        # Create a frequency index map of chars in p
        p_set = {}
        for char in p:
            p_set[char] = p_set.get(char, 0) + 1
        
        # def is_anagram_of_p(val):
        #     curr_window_is_anagram = True
        #     for i in range(len(val)):
        #         if val[i] not in p_set:
        #             curr_window_is_anagram = False
        #             break
        #     return curr_window_is_anagram
        
         # Initiate the initil sliding window in s
        left = 0
        curr_window = s[left:k]
        # Create frequency index map of this sliding window
        window_map = {}
        for char in curr_window:
            window_map[char] = window_map.get(char, 0) + 1
        
        # Check if this initial window is an anagram
        def isValidAnagram():
            for key in window_map.keys():
                if window_map[key] != p_set.get(key, 0):
                    return False
            return True

        if isValidAnagram():
            output.append(0)

        for right in range(k, len(s)):
            # Remove left most element from window_map
            if s[left] in window_map:
                window_map[s[left]] -= 1
            # Add the current right element
            window_map[s[right]] = window_map.get(s[right], 0) + 1
            if isValidAnagram():
                output.append(left+1)
            
            left += 1


        return output    




            


        