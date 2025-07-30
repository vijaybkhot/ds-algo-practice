class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        anagram_map = defaultdict(list)
        # for idx, word in enumerate(words):
        #     anagram = word.sort()
        #     anagram_map[anagram].append(idx)
        
        res = []
        for i in range(len(words)-1, 0, -1):
            anagram = ''.join(sorted(words[i]))
            prev_anagram = ''.join(sorted(words[i-1]))
            if anagram == prev_anagram:
                continue
            res.append(words[i])
        res.append(words[0])
        return res[::-1]
            