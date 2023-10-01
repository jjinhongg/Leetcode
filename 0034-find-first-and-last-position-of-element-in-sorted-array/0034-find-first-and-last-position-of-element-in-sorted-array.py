class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0 
        end = len(nums)-1
        res = [-1,-1]

        # Find first Index
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid]<target:
                start = mid + 1
            else:
                end = mid -1

        # Reset end to last idex
        end = len(nums)-1

        # Find Last Index
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid]>target:
                end = mid -1
            else:
                start = mid + 1

        return res