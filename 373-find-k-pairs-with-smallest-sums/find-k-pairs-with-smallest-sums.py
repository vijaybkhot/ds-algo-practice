class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Brute Force approach
        res = []
        pairs = []

        # # Optimized approach:
        # for i in range(min(len(nums1), k)):
        #     heapq.heappush(pairs, (nums1[i]+nums2[0], i, 0))

        # while pairs and len(res) < k:
        #     curr_sum, i, j = heapq.heappop(pairs)
        #     res.append([nums1[i], nums2[j]])

        #     if j+1 < len(nums2):
        #         next_sum = nums1[i]+nums2[j+1]
        #         heapq.heappush(pairs, (next_sum, i, j+1))

        # return res 

        # Appraoch Similar to Djikstras
        visited = set()
        heapq.heappush(pairs, (nums1[0]+nums2[0], 0, 0))
        visited.add((0, 0))

        while pairs and len(res)<k:
            curr_sum, i, j = heapq.heappop(pairs)
            res.append([nums1[i], nums2[j]])
            if j+1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(pairs, (nums1[i]+nums2[j+1], i, j+1))
            
            if i+1 < len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(pairs, (nums1[i+1]+nums2[j], i+1, j))
        
        return res


        
