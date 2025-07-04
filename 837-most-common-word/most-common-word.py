class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        i=0
        word_dict = defaultdict(int)
        max_count = 0
        banned_words = set(banned)
        while i < len(paragraph):
            curr_word = ""
            while i < len(paragraph) and (paragraph[i] not in "!?',;." and paragraph[i] != " "):
                curr_word += paragraph[i]
                i += 1
            curr_word = curr_word.lower()
            if curr_word not in banned_words:
                word_dict[curr_word.lower()] += 1
                max_count = max(max_count, word_dict[curr_word.lower()])
            while i < len(paragraph) and (paragraph[i] in "!?',;." or paragraph[i] == " "):
                i += 1
        res = ""
        # return word_dict
        for word, freq in word_dict.items():
            if freq == max_count:
                return word
        

        
        