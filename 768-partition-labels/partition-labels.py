class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_idx_map = defaultdict(int)
        for i in range(len(s)):
            max_idx_map[s[i]] = i
        

        start = 0
        i = 0
        res = []
        end = max_idx_map[s[0]]
        while i < len(s):
            if i == end:
                res.append(end-start+1)
                start = end + 1
                end = max_idx_map[s[start]] if start < len(s) else len(s)-1
            else:
                end = max(end, max_idx_map[s[i]])
            i += 1
        
        return res


























#         last_index = {}    # {char: last_index}
#         res = []
#         for index, char in enumerate(s):
#             last_index[char] = index
        
#         end = last_index[s[0]]
#         start = 0
#         for index, char in enumerate(s):
#             if index == end:
#                 res.append(end - start + 1)
#                 start = end + 1
#                 end = last_index[s[start]] if start < len(s) else index
#             else:
#                 end = max(end, last_index[s[index]])
            
#         return res

        