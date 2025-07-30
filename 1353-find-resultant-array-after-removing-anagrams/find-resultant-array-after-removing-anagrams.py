class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:        
        # res = []
        # for i in range(len(words)-1, 0, -1):
        #     anagram = ''.join(sorted(words[i]))
        #     prev_anagram = ''.join(sorted(words[i-1]))
        #     if anagram == prev_anagram:
        #         continue
        #     res.append(words[i])
        # res.append(words[0])
        # return res[::-1]
            
        # res = []
        # prev_freq = None
        # for word in words:
        #     curr_freq = tuple(sorted(Counter(word).items())) 
        #     if curr_freq != prev_freq:
        #         res.append(word)
        #         prev_freq = curr_freq
        # return res

        res = []
        prev_freq = None
        for word in words:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            if freq != prev_freq:
                res.append(word)
                prev_freq = freq
        return res
