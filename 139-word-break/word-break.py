class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # end = 0
        # start = 0
        # word_set = set(wordDict)
        # words = []
        # for end in range(len(s)):
        #     if s[start:end] in word_set:
        #         start = end

        # start = len(s)-1
        # while start > -1:
        #     if s[:start] in word_set and 
        #     if s[start:] in word_set:
        #         s = s[:start]
        #     start -= 1

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