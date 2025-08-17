class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        #               (i,"leet")
        #   l   e   e   t   c   o   d   e

        @lru_cache(None)
        def dfs(i, curr_word):
            if i >= n: 
                if curr_word not in word_set:
                    return False
                else:
                    return True

            if curr_word in word_set:
                return dfs(i, "") or dfs(i+1, curr_word+s[i])
            else:
                return dfs(i+1, curr_word+s[i])
        
        return dfs(0, "")