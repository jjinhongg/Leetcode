from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxFruits = 0
        fruit_count = defaultdict(int)
        
        for right in range(len(fruits)):
            # Add the fruit at the 'right' to the 'window'
            fruit_count[fruits[right]] += 1
            
            # While we have more than 2 types of fruits in the 'window',
            # remove fruits from the 'left'
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            # Update the maximum number of fruits that can be collected
            maxFruits = max(maxFruits, right - left + 1)
        
        return maxFruits
