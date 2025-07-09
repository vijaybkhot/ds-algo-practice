class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        widths = [w for w, h in envelopes]
        heights = [h for w, h in envelopes]
        n = len(envelopes)

        lis = []
        for h in heights:
            
            if lis and lis[-1] < h or (not lis):
                lis.append(h)
            else:
                idx = bisect_left(lis, h)
                lis[idx] = h
        return len(lis)

        # def next_idx(i):
        #     for j in range(i + 1, n):
        #         if widths[j] > widths[i] and heights[j] > heights[i]:
        #             return j
        #     return n

        # @lru_cache(None)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     next_valid_idx = next_idx(i)
        #     take = 1 + dfs(next_valid_idx)
        #     skip = dfs(i+1)
        #     return max(take, skip)
                
        # return dfs(0)