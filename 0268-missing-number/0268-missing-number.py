class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # solve with Hash map
        n = len(nums)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for i in range(n):
            if i not in freq:
                return i
            
        return n

