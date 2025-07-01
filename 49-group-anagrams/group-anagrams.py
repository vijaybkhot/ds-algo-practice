class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_strs = [(''.join(sorted(s)), s) for s in strs]

        anagram_strs.sort()
        res = []
        res.append([anagram_strs[0][1]])
        for i in range(1 ,len(strs)):
            anagram, s = anagram_strs[i]
            if anagram == anagram_strs[i-1][0]:
                res[-1].append(s)
            else:
                res.append([s])
        
        return res
