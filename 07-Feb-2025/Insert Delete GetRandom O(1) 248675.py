# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:
    import random
    def __init__(self):
        self.hashmap = {}
        self.list_el = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.list_el.append(val)
            self.hashmap[val] = len(self.list_el)-1

            return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            
            num_idx = self.hashmap[val]
            
            self.list_el[-1],self.list_el[num_idx] = self.list_el[num_idx], self.list_el[-1]


            self.hashmap[self.list_el[num_idx]] = self.hashmap[val]

            del self.hashmap[val]

            self.list_el.pop()
            return True

        else:
            return False

    def getRandom(self) -> int:
        n = random.randint(0, len(self.list_el)-1)
        
        return self.list_el[n]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()