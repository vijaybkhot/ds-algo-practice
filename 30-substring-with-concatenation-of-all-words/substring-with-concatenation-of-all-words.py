class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        k = len(words[0])
        num_words = len(words)
        word_map = Counter(words)
        
        # def all_words(i):
        #     curr_map = Counter()
        #     if i + (k * num_words) > len(s):
        #         return False
        #     for j in range(i, i + (k * num_words), k):
        #         curr_word = s[j:j+k]
        #         if curr_word in word_map:
        #             if curr_map[curr_word] + 1 > word_map[curr_word]:
        #                 return False
        #             curr_map[curr_word] += 1
        #         else:
        #             return False
        #     return True

        # res = []
        # for i in range(len(s) - k * num_words + 1):
        #     if all_words(i):
        #         res.append(i)
        
        # return res

        
        res = []
        for i in range(k):
            curr_map = Counter()
            for right in range(i, i+(k * num_words), k):
                curr_word = s[right:right+k]
                curr_map[curr_word] += 1
            
            left = i
            if curr_map == word_map:
                res.append(i)
            for right in range(i+(k * num_words), len(s), k):
                left_word = s[left:left+k]
                curr_map[left_word] -= 1
                left += k
                right_word = s[right:right+k]
                curr_map[right_word] += 1
                if curr_map == word_map:
                    res.append(left)
            
        return res


        
                

