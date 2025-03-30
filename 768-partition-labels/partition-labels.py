class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}    # {char: last_index}
        res = []
        for index, char in enumerate(s):
            last_index[char] = index
        
        end = last_index[s[0]]
        start = 0
        for index, char in enumerate(s):
            if index == end:
                res.append(end - start + 1)
                start = end + 1
                end = last_index[s[start]] if start < len(s) else index
            else:
                end = max(end, last_index[s[index]])
            
        return res

        