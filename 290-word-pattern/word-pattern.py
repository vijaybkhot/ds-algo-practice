class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = defaultdict(str)
        word_map = defaultdict(str)

        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            curr_pattern = pattern[i]
            word = s_list[i]
            if curr_pattern in pattern_map or word in word_map:
                if curr_pattern not in pattern_map or word not in word_map:
                    return False
                if pattern_map[curr_pattern] != word or word_map[word] != curr_pattern:
                    return False
            elif curr_pattern not in pattern_map and word not in word_map:
                word_map[word] = curr_pattern
                pattern_map[curr_pattern] = word
        
        return True
        