from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        counter = Counter()
        p_counter = Counter(p)

        res = []

        for right in range(len(s)):
            counter[s[right]] += 1

            while right-left+1 > len(p):
                counter[s[left]] -= 1
                left += 1
            
            if counter == p_counter:
                res.append(left)
        
        return res
