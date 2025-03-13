class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        for i in range(len(s)):
            char_map[s[i]] = t[i]
        
        # Check if multiple characters map to same character
        val_set = set(char_map.values())
        if len(val_set) != len(char_map):
            return False
        # Using the mapped words, create a new string from s
        new_str = ""
        for char in s:
            new_str = new_str + char_map[char]
        
        return new_str == t
        