class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # # Brute force
        # count = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if lower <= nums[i] + nums[j] <= upper:
        #             count += 1
        
        # return count

        # # Optimized solution:
        # count = 0
        # index_dict = {}
        # for index, num in enumerate(nums):
        #     if num not in index_dict:
        #         index_dict[num] = []
        #     index_dict[num].append(index)
        
        # unique_nums =  list(index_dict.keys())
        # unique_nums.sort()
        # # return unique_nums
        # for i in range(len(unique_nums)):
        #     if lower <= 2 * unique_nums[i] <= upper:
        #         count += math.comb(len(index_dict[unique_nums[i]]), 2)

        #     for j in range(i+1, len(unique_nums)):
        #         if lower <= unique_nums[i] + unique_nums[j] <= upper:
        #             if index_dict[unique_nums[i]][0] < index_dict[unique_nums[j]][-1]:
        #                 count += (len(index_dict[unique_nums[i]]) * len(index_dict[unique_nums[j]]))
        #         if unique_nums[i] + unique_nums[j] > upper:
        #             break
                
        # return count

        count = 0
        def binary_left_most(idx, target):
            left, right = idx+1, len(nums)-1
            res = len(nums)
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res
        
        def binary_right_most(idx, target):
            left, right = idx+1, len(nums)-1
            res = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] <= target:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res


        nums.sort()
        for i in range(len(nums)):
            l = binary_left_most(i, lower - nums[i])
            r = binary_right_most(i, upper - nums[i])
            if l <= r:
                count += (r - l + 1)

        return count
