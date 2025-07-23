class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # num_op = 0
        # l, r = 0, len(nums)-1

        # while l < r:
        #     curr_sum = nums[l]+nums[r]
        #     if curr_sum == k:
        #         l += 1
        #         r -= 1
        #         num_op += 1
        #     elif curr_sum < k:
        #         l += 1
        #     else:
        #         r -= 1
        
        # return num_op
        # # Brute force
        # counter = Counter(nums)
        # ops = 0
        # while counter:
        #     isOperation = False
        #     keys = list(counter.keys())  # ✅ Make a static copy
        #     for first in keys:
        #         second = k - first
        #         if second in counter:
        #             # Special case: when first == second, need at least 2 occurrences
        #             if first == second and counter[first] < 2:
        #                 continue
        #             counter[first] -= 1
        #             counter[second] -= 1
        #             if counter[first] == 0:
        #                 del counter[first]
        #             if counter.get(second, 0) == 0:
        #                 counter.pop(second, None)
        #             ops += 1
        #             isOperation = True
        #             break
        #     if not isOperation:
        #         break

        # return ops

        counter = Counter(nums)
        ops = 0

        for num in list(counter.keys()):
            complement = k - num
            if complement not in counter:
                continue

            if num == complement:
                count = counter[num] // 2
            else:
                count = min(counter[num], counter[complement])

            ops += count
            counter[num] -= count
            counter[complement] -= count

        return ops