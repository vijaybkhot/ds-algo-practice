class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        if triplets[0] == target:
            return True
        
        for i in range(1, n):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                triplets[i] = triplets[i-1]
                continue

            max_1, max_2, max_3 = max(triplets[i][0], triplets[i-1][0]), max(triplets[i][1], triplets[i-1][1]), max(triplets[i][2], triplets[i-1][2])

            min_1, min_2, min_3 = min(triplets[i][0], triplets[i-1][0]), min(triplets[i][1], triplets[i-1][1]), min(triplets[i][2], triplets[i-1][2])

            if [max_1, max_2, max_3] == target:
                return True
            new_triplet = []
            if max_1 <= target[0]:
                new_triplet.append(max_1)
            else:
                new_triplet.append(min_1)
            
            if max_2 <= target[1]:
                new_triplet.append(max_2)
            else:
                new_triplet.append(min_2)
            
            if max_3 <= target[2]:
                new_triplet.append(max_3)
            else:
                new_triplet.append(min_3)
            triplets[i] = new_triplet
        
        return False

