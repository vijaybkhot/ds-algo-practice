class RandomizedSet:

    def __init__(self):
        self.dict = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.list.append(val)
            idx = len(self.list)-1
            self.dict[val] = idx
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.dict:
            # Swap this with the last element in the list
            val_idx = self.dict[val]
            last_val_idx = len(self.list)-1
            last_val = self.list[last_val_idx]
            self.dict[val] = last_val_idx
            self.dict[last_val] = val_idx
            self.list[last_val_idx], self.list[val_idx] =  self.list[val_idx], self.list[last_val_idx]
            del self.dict[val]
            self.list.pop()
            return True
        return False
        
    def getRandom(self) -> int:
        return_idx = random.randrange(0, len(self.list))
        return self.list[return_idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()