class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        if len(strs) == 0:
            return output
        if len(strs) == 1: 
            return strs[0]

        sorted_strs = sorted(strs)
        min_range = min (len(sorted_strs[0]), len(sorted_strs[-1]))
        
        for i in range(min_range):
            if sorted_strs[0][i] == sorted_strs[-1][i]:
                output = output + sorted_strs[0][i]
            else:
                break

        return output