class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # basket_heap = [(idx, capacity) for idx, capacity in enumerate(baskets)]
        # heapq.heapify(basket_heap)
        # i, j, = 0, 0
        # unplaced = 0

        # n = len(fruits)
        # for fruit_count in fruits:
        #     backup = []
        #     while basket_heap and basket_heap[0][1] < fruit_count:
        #         backup.append(heapq.heappop(basket_heap))
        #     if basket_heap:
        #         heapq.heappop(basket_heap)
        #     elif not basket_heap:
        #         unplaced += 1
        #     while backup:
        #         heapq.heappush(basket_heap, heapq.heappop(backup))
        
        # return unplaced

        count = 0
        n = len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break
            count += unset
        return count