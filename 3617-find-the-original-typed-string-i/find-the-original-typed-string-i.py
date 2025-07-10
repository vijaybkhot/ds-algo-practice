class Solution:
    def possibleStringCount(self, word: str) -> int:
        counter = Counter(word)
        res = 1
        
        i = len(word)-2

        while i >= 0:
            if word[i] == word[i+1]:
                res += 1
            i -= 1
        
        return res