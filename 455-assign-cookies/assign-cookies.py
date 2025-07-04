class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = 0
        i = 0
        for idx, greed in enumerate(g):
            while i < len(s) and s[i] < greed:
                i += 1
            if i < len(s) and s[i] >= greed:
                content += 1
                i += 1
        
        return content
        