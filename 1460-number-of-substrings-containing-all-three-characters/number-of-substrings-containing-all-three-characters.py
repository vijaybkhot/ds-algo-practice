class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = defaultdict(int)
        res = 0
        left = 0

        n = len(s)
        for right in range(n):
            counter[s[right]] += 1
            while len(counter) == 3:
                res += n - right
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
        
        return res
            