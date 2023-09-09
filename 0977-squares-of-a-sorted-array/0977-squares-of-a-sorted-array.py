class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            # compare the absolute values of the elements at left and right pointers
            if abs(nums[left]) > abs(nums[right]):
                # insert the larger squared value at the end of result
                result[right - left] = nums[left] ** 2
                left += 1
            else:
                # insert the larger squared value at the end of result
                result[right - left] = nums[right] ** 2
                right -= 1

        return result

