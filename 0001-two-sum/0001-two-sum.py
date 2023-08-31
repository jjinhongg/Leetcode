class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
        return []
