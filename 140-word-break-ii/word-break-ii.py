class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        s_list = [char for char in s]

        wordSet = set(wordDict)
        
        def dfs(curr_index, start, path):
            if curr_index == len(s):
                if ''.join(s_list[start:curr_index]) in wordSet:
                    path += ''.join(s_list[start:curr_index])
                    res.append(path)
                return
            

            if ''.join(s_list[start:curr_index+1]) in wordSet:
                dfs(curr_index+1, curr_index+1, path + ''.join(s_list[start:curr_index+1]) + ' ')

            dfs(curr_index+1, start, path)
        
        dfs(0, 0, "")
        return res


            

