class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            leftAbs, rightAbs = abs(nums[l]), abs(nums[r])
            if leftAbs > rightAbs:
                answer.appendleft(leftAbs**2)
                l += 1
                
            else:
                answer.appendleft(rightAbs**2)
                r -= 1
                
        return list(answer)
        

