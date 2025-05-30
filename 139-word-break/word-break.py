class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # word_set = set(wordDict)
        # start = 0
        # for end in range(1, len(s)+1):
        #     if s[start:end] in word_set:
        #         start = end
            

        # return start == end


        # # Top-down DP
        # wordSet = set(wordDict)
        # memo = set()

        # def dfs(start):
        #     if start in memo:
        #         return False
        #     if start == len(s):
        #         return True

        #     for end in range(start + 1, len(s) + 1):
        #         if s[start:end] in wordSet and dfs(end):
        #             return True

        #     memo.add(start)  # mark this start as leading to a dead end
        #     return False

        # Bottom-up DP
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

        return dfs(0)





