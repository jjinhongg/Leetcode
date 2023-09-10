from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array in ascending order
        nums.sort()
        # initialize an empty list to store the triplets
        result = []
        # loop through the array from left to right
        for i in range(len(nums) - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        # return the result list
        return result

