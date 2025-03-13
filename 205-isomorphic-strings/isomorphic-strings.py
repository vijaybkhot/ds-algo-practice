class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # char_map = {}
        # for i in range(len(s)):
        #     char_map[s[i]] = t[i]
        
        # # Check if multiple characters map to same character
        # val_set = set(char_map.values())
        # if len(val_set) != len(char_map):
        #     return False
        # # Using the mapped words, create a new string from s
        # new_str = ""
        # for char in s:
        #     new_str = new_str + char_map[char]
        
        # return new_str == t
        
        # More optimized solution using two dictionaries
        if len(s) != len(t):
            return False
        
        map_s_to_t = {}
        map_t_to_s = {}
        
        for i in range(len(s)):
            # Check if there's a conflict in mapping from s to t
            if s[i] in map_s_to_t and map_s_to_t[s[i]] != t[i]:
                return False
            # Check if there's a conflict in mapping from t to s
            if t[i] in map_t_to_s and map_t_to_s[t[i]] != s[i]:
                return False
            
            # Map characters from s to t and t to s
            map_s_to_t[s[i]] = t[i]
            map_t_to_s[t[i]] = s[i]
        
        return True