class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for char in s_counter:
            if char not in t_counter or s_counter[char] != t_counter[char]:
                return False
        
        for char in t_counter:
            if char not in s_counter or s_counter[char] != t_counter[char]:
                return False
        
        return True