class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0]*26
        s2_map = [0]*26

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
        
        # for i in range(len(s2)):
        #     s2_map[ord(s2[i]) - ord('a')] += 1
        
        left = 0

        for right in range(len(s2)):
            s2_map[ord(s2[right]) - ord('a')] += 1

            while left <= right and right - left + 1 > len(s1):
                s2_map[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(s1) and s2_map == s1_map:
                return True
        
        return False