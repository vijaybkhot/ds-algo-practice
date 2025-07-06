class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.dict1 = Counter(nums1)
        self.dict2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.dict2[old_val] -= 1
        if self.dict2[old_val] == 0:
            del self.dict2[old_val]

        self.nums2[index] = new_val
        self.dict2[new_val] += 1     
        

    def count(self, tot: int) -> int:        
        count = 0
        for n2 in self.dict1:
            n1 = tot - n2
            if n1 in self.dict2:
                count += self.dict2[n1] * self.dict1[n2]
        return count


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)