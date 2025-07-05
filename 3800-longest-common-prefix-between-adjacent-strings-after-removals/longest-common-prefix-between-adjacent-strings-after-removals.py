class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def count_prefix(s1, s2):
            l, r = 0, 0
            count = 0
            while l < len(s1) and r < len(s2):
                if s1[l] == s2[r]:
                    count += 1
                    l += 1
                    r += 1
                else:
                    break
            return count
        
        prefix = [0]*len(words)
        suffix = [0]*len(words)
        
        for i in range(1, len(words)):
            prefix[i] = count_prefix(words[i], words[i-1])
        for i in range(len(words)-2, -1, -1):
            suffix[i] = count_prefix(words[i], words[i+1])
        
        max_prefix_up_to = [0]*len(words)
        max_suffix_from = [0]*len(words)
        res = [0]*len(words)
        for i in range(1, len(words)):
            max_prefix_up_to[i] = max(max_prefix_up_to[i-1], prefix[i])
        
        for i in range(len(words)-2, -1, -1):
            max_suffix_from[i] = max(max_suffix_from[i+1], suffix[i])
        
        n = len(words)
        for i in range(len(words)):
            left_max = max_prefix_up_to[i-1] if i > 0 else 0
            right_max = max_suffix_from[i+1] if i < n - 1 else 0
            mid = count_prefix(words[i-1], words[i+1]) if 0 < i < n - 1 else 0
            res[i] = max(left_max, right_max, mid)

        return res

