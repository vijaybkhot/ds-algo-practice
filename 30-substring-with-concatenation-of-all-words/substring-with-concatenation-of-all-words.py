class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # curr_set = set()
        # word_set = set(words)
        # word_len = len(words[0])
        # index_arr = []
        # index_map = defaultdict(int)
        # i = 0
        # while i < len(s):
        #     if s[i:i+word_len] in word_set:
        #         index_arr.append( s[i:i+word_len])
        #         index_map[len(index_arr)-1] = i 
        #         i += word_len
        #     else:
        #         index_arr.append( s[i])
        #         i += 1

        
        # left = 0
        # curr_set = set()
        # res = []
        # for right in range(len(index_arr)):
        #     curr_word = index_arr[right]
        #     if curr_word not in word_set:
        #         left = right+1
        #         curr_set = set()
        #     else:
        #         while left < right and index_arr[right] in curr_set:
        #             curr_set.remove(index_arr[left])
        #             left += 1
        #         curr_set.add(index_arr[right])
        #         if len(curr_set) == len(words):
        #             res.append(index_map[left])
        # return res
                
        if not s or not words:
            return []
        
        words_map = Counter(words)
        word_len = len(words[0])
        res = []

        for i in range(len(s) - len(words) * word_len + 1):
            curr_word = s[i:i+word_len]
            curr_count = Counter()
            if curr_word in words_map:
                is_valid = True
                for j in range(i, i+(len(words)*word_len), word_len):
                    word = s[j:j+word_len]
                    if word not in words_map:
                        is_valid = False
                        break
                    else:
                        curr_count[word] += 1
                    
                if not is_valid:
                    continue
                if curr_count == words_map:
                    res.append(i)
        return res




