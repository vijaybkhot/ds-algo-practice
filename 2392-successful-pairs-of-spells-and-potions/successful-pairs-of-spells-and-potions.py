class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        

        def bs_left(arr, target):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid+1
            return left
        
        

        pairs = []
        potions.sort()

        for idx, spell in enumerate(spells):
            required_potion_strength = success/spell
            # potion_idx = bisect_left(potions, required_potion_strength)
            potion_idx = bs_left(potions, required_potion_strength)
            if potion_idx > len(potions):
                continue
            pairs.append(len(potions)-potion_idx)

        return pairs

        