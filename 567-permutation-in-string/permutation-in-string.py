class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        for char in s1:
            s1_map[char] += 1
        
        left = 0
        for i in range(len(s1)):
            s2_map[s2[i]] += 1
        if s1_map == s2_map:
            return True
        
        for right in range(len(s1), len(s2)):
            # remove left pointer element
            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]
            left += 1
            # add right element
            s2_map[s2[right]] += 1
            if s1_map == s2_map:
                return True
        
        return False