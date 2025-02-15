class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        # """

        # # O(n*k log k) solution
        # # Convert the anagrams to words which have characters in sorted order
        # sorted_anagrams = []
        # for string in strs:
        #     charArray = list(string)
        #     sorted_char_array = sorted(charArray)
        #     sorted_anagrams.append("".join(sorted_char_array))
        # # Create hash map of the sorted anagrams with theri index
        # sorted_anagram_dict = {}
        # for i in range (len(sorted_anagrams)):
        #     if sorted_anagrams[i] in sorted_anagram_dict:
        #         sorted_anagram_dict[sorted_anagrams[i]].append(i)
        #     else:
        #         sorted_anagram_dict[sorted_anagrams[i]] = [i]
        # result = []
        # for anagram_group_indices in sorted_anagram_dict.values():
        #     anagramGroupArray = [strs[index] for index in anagram_group_indices]
        #     result.append(anagramGroupArray)
        
        # return result

        # Create an empty alphabet dictionary:
        # alphabet_dict = {a:0, b:0, c:0, d:0, e:0, f:0, g:0, h:0, i:0, j:0, k:0, l:0, m:0, n:0, o:0, p:0, q:0, r:0, s:0, t:0, u:0, v:0, w:0, x:0, y:0, z:0}

        # def getAlphabetFrequency(word):
        #     curr_aplha_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
        #     word_char__list = list(word)
        #     for char in word_char__list:
        #         curr_aplha_dict[char.lower()] += 1
        #     return curr_aplha_dict

        def getAlphabetFrequency(word):
            curr_aplha_dict = {}
            for char in word:
                lower_char = char.lower()
                if lower_char in curr_aplha_dict:
                    curr_aplha_dict[lower_char] += 1
                else:
                    curr_aplha_dict[lower_char] = 1
            return curr_aplha_dict
        
        # loop over all words in list to get alphabet frequency dict
        anagram_map = {}
        for i in range (len(strs)):
            alpha_freq_dict = getAlphabetFrequency(strs[i])
            sorted_alpha_freq_dict = dict(sorted(alpha_freq_dict.items()))
            tuple_of_tuples = tuple(sorted_alpha_freq_dict.items())
            if tuple_of_tuples in anagram_map:
                anagram_map[tuple_of_tuples].append(i)
            else:
                anagram_map[tuple_of_tuples] = [i]
        
        # Get the indices of each anagram from the anagram_map and group all the words from strs having same anagram together

        result = []

        for anagram_index_array in anagram_map.values():
            result.append([strs[index] for index in anagram_index_array])
        return result



        





            






            

