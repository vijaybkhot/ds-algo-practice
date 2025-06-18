class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        
        frequency_dict = defaultdict(int)
        for num in hand:
            frequency_dict[num] += 1
        min_heap = list(frequency_dict.keys())
        heapq.heapify(min_heap)
        
        while frequency_dict:
            while min_heap and frequency_dict[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            if not min_heap:
                break

            min_card = min_heap[0]
            for i in range(groupSize):
                card = min_card + i
                if frequency_dict[card] == 0:
                    return False
                frequency_dict[card] -= 1
        
        return True