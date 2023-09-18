from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict()
        duplicates = []
        
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
                
            else:
                hash_map[n] += 1
                duplicates.append(n)
                
        # for i in range(1,len(nums)+1):
        #     if hash_map[i] and hash_map[i] == 2:
        #         duplicates.append(i)
            
        return duplicates
        