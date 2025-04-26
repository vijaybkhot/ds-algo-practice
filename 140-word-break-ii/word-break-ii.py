class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # # First attempt
        # res = []
        # s_list = [char for char in s]

        # wordSet = set(wordDict)
        
        # def dfs(curr_index, start, path):
        #     if curr_index == len(s)-1:
        #         if ''.join(s_list[start:curr_index+1]) in wordSet:
        #             path += ''.join(s_list[start:curr_index+1])
        #             res.append(path)
        #         return
            

        #     if ''.join(s_list[start:curr_index+1]) in wordSet:
        #         dfs(curr_index+1, curr_index+1, path + ''.join(s_list[start:curr_index+1]) + ' ')

        #     dfs(curr_index+1, start, path)
        
        # dfs(0, 0, "")
        # return res

        # res = []
        # wordSet = set(wordDict)
        
        # def dfs(curr_index, start, path):
        #     if curr_index == len(s):
        #         if s[start:curr_index] in wordSet:
        #             path += s[start:curr_index]
        #             res.append(path)
        #         return
            

        #     if s[start:curr_index+1] in wordSet:
        #         dfs(curr_index+1, curr_index+1, path + s[start:curr_index+1] + ' ')

        #     dfs(curr_index+1, start, path)
        
        # dfs(0, 0, "")
        # return res
        res = []
        wordSet = set(wordDict)

        def dfs(start, end, path):
            if start == len(s):
                res.append(path.strip())
                return

            for i in range(end, len(s)):
                if s[start:i+1] in wordSet:
                    dfs(i+1, i+1, path + s[start:i+1] + " ")

        dfs(0, 0, "")
        return res

                

