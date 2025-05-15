class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        count = 0
        res = []
        i, j = 0, 1
        if words:
            res.append(words[i])
        while j < len(groups):
            if groups[j] != groups[i]:
                res.append(words[j])
                i = j
            j += 1

        
        return res
        
