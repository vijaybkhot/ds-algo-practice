class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        
        frequency_dict = defaultdict(int)
        for num in hand:
            frequency_dict[num] += 1
        
        while frequency_dict:
            min_card = min(frequency_dict)
            for i in range(groupSize):
                card = min_card + i
                if frequency_dict[card] == 0:
                    return False
                frequency_dict[card] -= 1
                if frequency_dict[card] == 0:
                    del frequency_dict[card]
        
        return True