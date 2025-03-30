class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charHashMap = {}    # {char: [first_index, last_index]}
        res = []
        for index, char in enumerate(s):
            if char not in charHashMap:
                charHashMap[char] = [index, index]
            else:
                charHashMap[char] = [charHashMap[char][0], index]
        
        curr_last_index = charHashMap[s[0]][1]
        i = 0
        for index, char in enumerate(s):
            if index == curr_last_index:
                res.append(index - i + 1)
                i = index + 1
                curr_last_index = charHashMap[s[index+1]][1] if index+1 < len(s) else index
            else:
                curr_last_index = max(curr_last_index, charHashMap[s[index]][1])
            
        return res



            
