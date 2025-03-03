class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # nums.sort()
        # n = len(nums)
        # res = []
        # for i in range(n):
        #     curr_num = nums[i]
        #     curr_target = -curr_num
        #     left, right = i + 1, n-1
        #     curr_triplet = []
        #     while left < right:
        #         if nums[left] + nums[right] == curr_target:
        #             curr_triplet = [nums[i], nums[left], nums[right]]
        #             if curr_triplet in res:
        #                 curr_triplet = []
        #             if len(curr_triplet) == 3:
        #                 res.append(curr_triplet)
        #             left += 1
        #             right -= 1 
        #         elif nums[left] + nums[right] < curr_target:
        #             left += 1
        #         else:
        #             right -= 1
        
        # return res

        # # Optimize above approach. Used a set to store first elem in each triplets, to avoid duplicates
        # nums.sort()
        # n = len(nums)
        # res = []
        # triplet_first = set()
        # for i in range(n):
        #     curr_num = nums[i]
        #     if curr_num in triplet_first:
        #         continue
        #     curr_target = -curr_num
        #     left, right = i + 1, n-1
        #     curr_triplet = []
        #     while left < right:
        #         if nums[left] + nums[right] == curr_target:
        #             curr_triplet = [nums[i], nums[left], nums[right]]
        #             if len(curr_triplet) == 3:
        #                 res.append(curr_triplet)
        #             left += 1
        #             while nums[left] == nums[left-1] and left < right:
        #                 left += 1
        #         elif nums[left] + nums[right] < curr_target:
        #             left += 1
        #         else:
        #             right -= 1
        #     triplet_first.add(curr_num)
        
        # return res

         # Optimize above approach. without using set
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            curr_num = nums[i]
            if i > 0 and curr_num == nums[i-1]:
                continue
            curr_target = -curr_num
            left, right = i + 1, n-1
            curr_triplet = []
            while left < right:
                if nums[left] + nums[right] == curr_target:
                    curr_triplet = [nums[i], nums[left], nums[right]]
                    if len(curr_triplet) == 3:
                        res.append(curr_triplet)
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif nums[left] + nums[right] < curr_target:
                    left += 1
                else:
                    right -= 1      

        return res

