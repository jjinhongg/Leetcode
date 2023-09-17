from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(lambda: "Not Present")
        missing = []
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
                
            else:
                hash_map[n] += 1
            
        for i in range(1,len(nums)+1):
            print(i)
            if i not in hash_map:
                missing.append(i)
                
        return missing
                
        