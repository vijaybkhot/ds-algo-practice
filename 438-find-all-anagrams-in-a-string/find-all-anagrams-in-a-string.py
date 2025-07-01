class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []
        anagrams = []
        left = 0
        p_map, s_map = defaultdict(int), defaultdict(int)
        for i in range(len_p):
            p_map[p[i]] += 1
            s_map[s[i]] += 1
        left = 0
        if p_map == s_map:
            anagrams.append(left)
        
        for right in range(len_p, len_s):
            # remove left char from s_map
            s_map[s[left]] -= 1
            if s_map[s[left]] == 0:
                del s_map[s[left]]
            left += 1
            # add right char to s_map
            s_map[s[right]] += 1
            if s_map == p_map:
                anagrams.append(left)
        
        return anagrams