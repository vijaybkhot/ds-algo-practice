class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
        p_map = dict()
        s_map = dict()

        for i in range(len(pattern)):
            char, word = pattern[i], s_list[i]
            if char not in p_map and word not in s_map:
                p_map[char] = word
                s_map[word] = char
            else:
                if char not in p_map or word not in s_map or p_map[char] != word or s_map[word] != char:
                    return False
        
        return True