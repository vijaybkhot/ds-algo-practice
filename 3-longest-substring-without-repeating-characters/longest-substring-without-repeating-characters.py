class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        res = 0
        left, right = 0, 1
        curr_set = set()
        curr_set.add(s[left])
        while left < len(s) and right < len(s):
            while right < len(s) and s[right] not in curr_set:
                curr_set.add(s[right])
                right += 1
                res = max(res, len(curr_set))
            while right < len(s) and s[right] in curr_set:
                curr_set.remove(s[left])
                left += 1
        
        return max(res, 1)





















        # res = 0
        # i, j = 0, 0
        # curr_set = set()
        
        # index_map = defaultdict(int)

        # for idx, char in enumerate(s):
        #     s[char] += 1
        
        # l, r = 0, len(s)-1
        
        # while l < r:
        #     if index_map[s[l]] > 1:
        #         l += 1
        #     if index_map[s[r]] > 1:
        #         r -= 1
            