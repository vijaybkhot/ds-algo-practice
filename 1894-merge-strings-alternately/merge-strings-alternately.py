class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i, j = 0, 0
        output = ""

        while i < len(word1) and j < len(word2):
            output += word1[i]
            output += word2[j]
            i += 1
            j += 1
        
        while i < len(word1):
            output += word1[i]
            i += 1
        
        while j < len(word2):
            output += word2[j]
            j += 1
        
        return output