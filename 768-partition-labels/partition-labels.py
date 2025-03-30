class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charHashMap = {}    # {char: [first_index, last_index]}
        res = []
        for index, char in enumerate(s):
            if char not in charHashMap:
                charHashMap[char] = [index, index]
            else:
                charHashMap[char] = [charHashMap[char][0], index]
        
        end = charHashMap[s[0]][1]
        start = 0
        for index, char in enumerate(s):
            if index == end:
                res.append(end - start + 1)
                start = end + 1
                end = charHashMap[s[start]][1] if start < len(s) else index
            else:
                end = max(end, charHashMap[s[index]][1])
            
        return res



            
