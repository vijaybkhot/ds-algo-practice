class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # Divide and conquer:
        def longest(subs, k):
            counter = Counter(subs)
            
            # if all characters meet requirement
            if all(count >= k for count in counter.values()):
                return len(subs)
            
            # find one bad character
            for bad_char, count in counter.items():
                if count < k:
                    # split on this bad char
                    return max(longest(seg, k) for seg in subs.split(bad_char))
            
            return 0  # should never reach here
        
        return longest(s, k)

        # # Sliding window approach
        # res = 0
        # for n in range(1, 27):
        #     count_at_least_k = 0
        #     left = 0
        #     curr_map = defaultdict(int)
        #     min_freq = 0
        #     for right in range(len(s)):
        #         curr_map[s[right]] += 1
        #         if curr_map[s[right]] == k:
        #             count_at_least_k += 1

        #         while left <= right and len(curr_map) > n:
        #             if curr_map[s[left]] == k:
        #                 count_at_least_k -= 1
        #             curr_map[s[left]] -= 1
        #             if curr_map[s[left]] == 0:
        #                 del curr_map[s[left]]
        #             left += 1
                
        #         if len(curr_map) == n and count_at_least_k == n:
        #             res = max(res, right - left + 1)
        
        # return res
            