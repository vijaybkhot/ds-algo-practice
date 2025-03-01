class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Create a hash set
        missing = 0
        curr_pos = 1
        arr_set = set(arr)
        while missing < k:
            if curr_pos not in arr_set:
                missing += 1
            if missing == k:
                break
            curr_pos += 1
        
        return curr_pos
        