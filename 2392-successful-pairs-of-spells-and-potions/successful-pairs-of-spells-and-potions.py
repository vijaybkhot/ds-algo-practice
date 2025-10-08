class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # spells = [5,1,3]

        # 1,2,3,4,5

        # success = 7

        


        pairs = []
        potions.sort()
        # return bisect_left(potions, 7/5)
        for idx, spell in enumerate(spells):
            required_potion_strength = success/spell
            potion_idx = bisect_left(potions, required_potion_strength)
            if potion_idx > len(potions):
                continue
            pairs.append(len(potions)-potion_idx)

        return pairs