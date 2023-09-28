class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Initialize low and high pointers
        low = 0
        high = len(letters) - 1

        # Loop until low and high meet
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2
            # Compare the middle element with the target
            if letters[mid] <= target:
                # If the middle element is smaller than or equal to the target, 
                # move the low pointer to the right
                low = mid + 1
            else:
                # If the middle element is greater than the target, 
                # move the high pointer to the left
                high = mid - 1

        # Return the element at the low pointer, or the first element if low is out of bounds
        return letters[low] if low < len(letters) else letters[0]
