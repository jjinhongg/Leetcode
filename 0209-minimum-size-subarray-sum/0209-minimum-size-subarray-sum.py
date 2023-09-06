class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                print(f'right: {right} \n left: {left} \n sum: {sum}')
                min_length = min(min_length, right - left + 1)
                print(f'min_length = {min_length}')
                sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
