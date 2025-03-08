class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""
        window = {}
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        need = len(t_map)
        have = 0
        res, resLen = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in t_map and window[char] == t_map[char]:
                have += 1
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                left_char = s[left]
                window[left_char] = window.get(left_char) - 1
                left += 1
                if left_char in t_map and window[left_char] < t_map[left_char]:
                    have -= 1
        
        return s[res[0]:res[1]+1]
        
                

