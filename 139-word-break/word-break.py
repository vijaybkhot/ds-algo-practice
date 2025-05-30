class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # word_set = set(wordDict)
        # start = 0
        # for end in range(1, len(s)+1):
        #     if s[start:end] in word_set:
        #         start = end
            

        # return start == end


        wordSet = set(wordDict)
        memo = set()

        def dfs(start):
            if start in memo:
                return False
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and dfs(end):
                    return True

            memo.add(start)  # mark this start as leading to a dead end
            return False

        return dfs(0)





