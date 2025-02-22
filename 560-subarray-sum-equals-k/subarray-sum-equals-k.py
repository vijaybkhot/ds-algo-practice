class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # # Brute force solution
        # res = 0
        # prefix_array = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix_array.append(prefix_array[i-1] + nums[i])

        # for num in prefix_array:
        #     if num == k:
        #         res += 1
        
        # for i in range(len(prefix_array)-1, 0, -1):
        #     for j in range(i-1, -1, -1):
        #         if prefix_array[i] - prefix_array[j] == k:
        #             res += 1

        # return res

        # Efficient solution:
        res = 0
        prefix_count = {0: 1}
        prefix_array = [0]
        for i in range(len(nums)):
            curr_prefix = prefix_array[-1] + nums[i]
            if curr_prefix-k in prefix_count:
                res += prefix_count[curr_prefix-k]
            prefix_array.append(curr_prefix)
            prefix_count[curr_prefix] = prefix_count.get(curr_prefix, 0) + 1
        
        return res


         


