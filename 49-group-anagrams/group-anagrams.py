class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        # """
        # # Function to create a character frequency dictionary:
        # def charFrequencyDict(string):
        #     charFreqDict = {}
        #     for char in string:
        #         if char in charFreqDict:
        #             charFreqDict[char] += 1
        #         else:
        #             charFreqDict[char] = 1
        #     return charFreqDict

        # # Get charFreqDicts for all strs
        # charFreqDictArray = []
        # for string in strs:
        #     charFreqDictArray.append(charFrequencyDict(string))
        
        # # Loop through the charFreqDictArray to find similar anagrams and group them
        # anagramGroupHashMap = {}
        # for i in range(len(strs)):
        #     currAnagramStr = (charFreqDictArray[i])
        #     if currAnagramStr in anagramGroupHashMap:
        #         anagramGroupHashMap[currAnagramStr].append(i)
        #     else:
        #         anagramGroupHashMap[currAnagramStr] = [i]
        
        # result = []
        # for anagramGroup in anagramGroupHashMap.values():
        #     anagramGroupArray = [strs[index] for index in anagramGroup]
        #     result.append(anagramGroupArray)
        
        # return result

        # Convert the anagrams to words which have characters in sorted order
        sorted_anagrams = []
        for string in strs:
            charArray = list(string)
            sorted_char_array = sorted(charArray)
            sorted_anagrams.append("".join(sorted_char_array))
        # Create hash map of the sorted anagrams with theri index
        sorted_anagram_dict = {}
        for i in range (len(sorted_anagrams)):
            if sorted_anagrams[i] in sorted_anagram_dict:
                sorted_anagram_dict[sorted_anagrams[i]].append(i)
            else:
                sorted_anagram_dict[sorted_anagrams[i]] = [i]
        result = []
        for anagram_group_indices in sorted_anagram_dict.values():
            anagramGroupArray = [strs[index] for index in anagram_group_indices]
            result.append(anagramGroupArray)
        
        return result
            






            

