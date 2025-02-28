class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        # max_element = max(nums)
        # count_array = [0] * (max_element + 1)

        # for num in nums:
        #     count_array[num] += 1
        # majority_value = len(nums)//3

        # for i in range(len(count_array)):
        #     if count_array[i] > majority_value:
        #         res.append(i)
        
        # return res
        # Create frequency index map
        def frequency_map(arr):
            hash_map = {}
            for num in arr:
                hash_map[num] = hash_map.get(num, 0) + 1
            return hash_map

        majority_value = len(nums)//3
        freq_index_map = frequency_map(nums)
        for key, value in freq_index_map.items():
            if value > majority_value:
                res.append(key)
        
        return res


        