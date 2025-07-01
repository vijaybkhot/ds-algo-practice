class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq_s = defaultdict(int)
        char_freq_t = defaultdict(int)
        for char in s:
            char_freq_s[char] += 1
        for char in t:
            char_freq_t[char] += 1
        
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char_freq_s[char] != char_freq_t[char]:
                return False
        
        return True
        