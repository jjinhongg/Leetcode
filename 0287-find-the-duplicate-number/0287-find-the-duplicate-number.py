from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = defaultdict()
        
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            
            else:
                hash_map[n] += 1
                return n
                
        
        