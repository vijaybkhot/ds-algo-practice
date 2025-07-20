class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Brute Force approach
        res = []
        pairs = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(pairs, (nums1[i]+nums2[0], i, 0))
    
        
        
        while pairs and len(res) < k:
            curr_sum, i, j = heapq.heappop(pairs)
            res.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                next_sum = nums1[i]+nums2[j+1]
                heapq.heappush(pairs, (next_sum, i, j+1))

        return res 

        
