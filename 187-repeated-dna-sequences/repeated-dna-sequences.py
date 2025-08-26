class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = Counter()
        curr_str = s[:10]
        counter[curr_str] += 1

        left = 0
        res = set()
        for right in range(10, len(s)):
            new_str = curr_str[1:] + s[right]
            if new_str in counter and new_str not in res:
                res.add(new_str)
            else:
                counter[new_str] += 1
            curr_str = new_str
        
        return list(res)

