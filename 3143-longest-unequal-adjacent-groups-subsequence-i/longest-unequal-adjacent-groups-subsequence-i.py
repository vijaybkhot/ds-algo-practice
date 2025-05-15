class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        count = 0
        res = []
        i, j = 0, 1
        start = False
        while j < len(groups):
            if groups[j] != groups[i]:
                if not start:
                    res.append(words[i])
                    start = True
                res.append(words[j])
                i = j
            j += 1
        if not res and words:
            res.append(words[0])
        
        return res
        
