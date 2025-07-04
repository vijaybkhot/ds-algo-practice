class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words_set = set(words)
        def canFormWord(word):
            dp = {}
            def dfs(start):
                if start in dp:
                    return dp[start]
                if start == len(word):
                    return True
                dp[start] = False
                for end in range(start, len(word)):
                    if word[start:end+1]in words_set and dfs(end+1):
                        dp[start] = True
                        return True
                
                return dp[start]
            return dfs(0)

        res = []

        for word in words:
            if word == "":
                continue
            words_set.remove(word)              # prevent self-match
            if canFormWord(word):
                res.append(word)
            words_set.add(word)
        
        return res

        
        # for word in words:
        #     i, j = len(word)-1, len(word)-1
        #     word_count = 0
        #     words_set.remove(word)
        #     while j >= 0 and i >= 0:
        #         if word[j:i+1] in words_set:
        #             i = j-1
        #             word_count += 1
        #         j -= 1
        #     if word_count > 1 and i < 0 and j < 0:
        #         res.append(word)
        #     words_set.add(word)
        
        # return res
        