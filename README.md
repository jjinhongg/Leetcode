# LeetCode Grokking Notes

I liked the way Grokking the coding interview organized problems into learnable patterns. However, the course is expensive and the majority of the time the problems are copy-pasted from leetcode. As the explanations on leetcode are usually just as good, the course really boils down to being a glorified curated list of leetcode problems.

So below is a tracker that I've made to track my learning progress of leetcode problems that are as close to grokking problems as possible. 

## Pattern: Sliding Window

- [x] https://leetcode.com/problems/maximum-subarray/ # Close enough
- [x] https://leetcode.com/problems/minimum-size-subarray-sum/
- [ ] https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
- [ ] https://leetcode.com/problems/fruit-into-baskets/
- [ ] https://leetcode.com/problems/longest-substring-without-repeating-characters/
- [ ] https://leetcode.com/problems/longest-repeating-character-replacement/
- [ ] https://leetcode.com/problems/max-consecutive-ones-iii/
- [ ] https://leetcode.com/problems/permutation-in-string/
- [ ] https://leetcode.com/problems/find-all-anagrams-in-a-string/
- [ ] https://leetcode.com/problems/minimum-window-substring/
- [ ] https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Pattern: Two Pointers

- [x] https://leetcode.com/problems/two-sum/
- [x] https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- [x] https://leetcode.com/problems/squares-of-a-sorted-array/
- [x] https://leetcode.com/problems/3sum/
- [x] https://leetcode.com/problems/3sum-closest/
- [ ] https://leetcode.com/problems/3sum-smaller/
- [ ] https://leetcode.com/problems/subarray-product-less-than-k/
- [ ] https://leetcode.com/problems/sort-colors/
- [ ] https://leetcode.com/problems/4sum/
- [ ] https://leetcode.com/problems/backspace-string-compare/
- [ ] https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

## Pattern: Fast & Slow pointers
- [ ] https://leetcode.com/problems/linked-list-cycle/
- [ ] https://leetcode.com/problems/linked-list-cycle-ii/
- [ ] https://leetcode.com/problems/happy-number/
- [ ] https://leetcode.com/problems/middle-of-the-linked-list/
- [ ] https://leetcode.com/problems/palindrome-linked-list/
- [ ] https://leetcode.com/problems/reorder-list/
- [ ] https://leetcode.com/problems/circular-array-loop/

## Pattern: Merge Intervals
- [ ] https://leetcode.com/problems/merge-intervals/
- [ ] https://leetcode.com/problems/insert-interval/
- [ ] https://leetcode.com/problems/interval-list-intersections/
- [ ] https://leetcode.com/problems/meeting-rooms-ii/
- [ ] Could not find equivalent. Given a list of intervals with values, find the peak sum (i.e. if intervals are overlapping, sum their values)
- [ ] https://leetcode.com/problems/employee-free-time/

## Pattern: Cyclic Sort

- [ ] Couldn't find equivalent for the first question. The second question below encompasses the first one though. See https://leetcode.com/problems/missing-number/discuss/859510/C%2B%2B-O(N)-O(1)-using-Cyclic-Sort for how grokking the coding interview approached these problems. It uses the fact that we can sort the array in O(n) without comparison operators
- [ ] https://leetcode.com/problems/missing-number/
- [ ] https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- [ ] https://leetcode.com/problems/find-all-duplicates-in-an-array/
- [ ] combine https://leetcode.com/problems/find-the-duplicate-number/ and https://leetcode.com/problems/missing-number/
- [ ] https://leetcode.com/problems/first-missing-positive/
- [ ] https://leetcode.com/problems/kth-missing-positive-number/

## Pattern: In-place Reversal of a LinkedList
- [x] https://leetcode.com/problems/reverse-linked-list/
- [ ] https://leetcode.com/problems/reverse-linked-list-ii/
- [ ] https://leetcode.com/problems/reverse-nodes-in-k-group/
- [ ] Next question is the same, but alternate each subgroup
- [ ] https://leetcode.com/problems/rotate-list/

## Pattern: Tree Breadth First Search
- [x] https://leetcode.com/problems/binary-tree-level-order-traversal/
- [ ] https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
- [ ] https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
- [ ] https://leetcode.com/problems/minimum-depth-of-binary-tree/
- [ ] https://leetcode.com/problems/inorder-successor-in-bst/  # Close, not exact
- [ ] https://leetcode.com/problems/populating-next-right-pointers-in-each-node/  # Close, grokk assumes non-perfect tree
- [ ] Next question is the same, but connect end nodes to the next level instead of null
- [ ] https://leetcode.com/problems/binary-tree-right-side-view/

## Pattern: Tree Depth First Search
- [ ] https://leetcode.com/problems/path-sum/
- [ ] https://leetcode.com/problems/path-sum-ii/
- [ ] https://leetcode.com/problems/sum-root-to-leaf-numbers/
- [ ] https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/description/
- [ ] https://leetcode.com/problems/path-sum-iii/
- [ ] https://leetcode.com/problems/diameter-of-binary-tree/
- [ ] https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Pattern: Two Heaps
- [ ] https://leetcode.com/problems/find-median-from-data-stream/
- [ ] https://leetcode.com/problems/sliding-window-median/
- [ ] https://leetcode.com/problems/ipo/
- [ ] https://leetcode.com/problems/find-right-interval/

## Pattern: Subsets
- [ ] https://leetcode.com/problems/subsets/
- [ ] https://leetcode.com/problems/subsets-ii/
- [ ] https://leetcode.com/problems/permutations/
- [ ] https://leetcode.com/problems/letter-case-permutation/
- [ ] https://leetcode.com/problems/generate-parentheses/
- [ ] https://leetcode.com/problems/generalized-abbreviation/
- [ ] https://leetcode.com/problems/different-ways-to-add-parentheses/
- [ ] https://leetcode.com/problems/unique-binary-search-trees-ii/
- [ ] https://leetcode.com/problems/unique-binary-search-trees/

## Pattern: Modified Binary Search
- [x] https://leetcode.com/problems/binary-search/  # Close enough. The grokking problem allows sorted input arrays as ascending or descending, which only introduces a simple check
- [ ] Did not find. Problem is find index of smallest element greater or equal to input value
- [ ] https://leetcode.com/problems/find-smallest-letter-greater-than-target/
- [ ] https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- [ ] https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
- [ ] https://leetcode.com/problems/find-k-closest-elements/ (with K == 1)
- [ ] https://leetcode.com/problems/peak-index-in-a-mountain-array/
- [ ] https://leetcode.com/problems/find-in-mountain-array/
- [ ] https://leetcode.com/problems/search-in-rotated-sorted-array/
- [ ] Similar to previous, but find the number of rotations of the array.

## Pattern: Bitwise XOR
- [x] https://leetcode.com/problems/single-number/
- [ ] https://leetcode.com/problems/single-number-iii/
- [ ] https://leetcode.com/problems/complement-of-base-10-integer/
- [ ] https://leetcode.com/problems/flipping-an-image/

## Pattern: Top 'K' elements
- [ ] Same as second question, but the first Grokking question wants the top K instead of the bottom K
- [ ] https://leetcode.com/problems/kth-largest-element-in-an-array
- [ ] https://leetcode.com/problems/k-closest-points-to-origin/
- [ ] https://leetcode.com/problems/minimum-cost-to-connect-sticks/
- [ ] https://leetcode.com/problems/top-k-frequent-elements/
- [ ] https://leetcode.com/problems/sort-characters-by-frequency/
- [ ] https://leetcode.com/problems/kth-largest-element-in-a-stream/
- [ ] https://leetcode.com/problems/find-k-closest-elements/
- [ ] https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/ closest leetcode or https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/ for exact
- [ ] https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/ no leetcode equivalent found
- [ ] https://leetcode.com/problems/reorganize-string/
- [ ] https://leetcode.com/problems/rearrange-string-k-distance-apart/
- [ ] https://leetcode.com/problems/task-scheduler/
- [ ] https://leetcode.com/problems/maximum-frequency-stack/

## Pattern: K-way merge
- [ ] https://leetcode.com/problems/merge-k-sorted-lists/
- [ ] Same as previous, but return the Kth smallest number
- [ ] https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
- [ ] https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
- [ ] https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ small difference, grokking has different sort order and wants the largest

## Pattern: 0/1 Knapsack
- [ ] https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RM1BDv71V60
- [ ] https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3jEPRo5PDvx or https://leetcode.com/problems/partition-equal-subset-sum/
- [ ] https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3j64vRY6JnR
- [ ] https://leetcode.com/problems/last-stone-weight-ii/ similar concept, but problem description is more abstract.
- [ ] https://leetcode.com/problems/combination-sum-ii/ similar, but return the number of combinations instead of the combinations
- [ ] https://leetcode.com/problems/target-sum/
- [ ] BONUS : Not in grokking, but I still found this very useful https://leetcode.com/problems/ones-and-zeroes/

## Pattern: Topological Sort
- [ ] First problem is identical to the following three
- [ ] https://leetcode.com/problems/course-schedule/
- [ ] https://leetcode.com/problems/course-schedule-ii/ 
* Same as above, but return all instead of any
- [ ] https://leetcode.com/problems/alien-dictionary/
- [ ] https://leetcode.com/problems/sequence-reconstruction/description/
- [ ] https://leetcode.com/problems/minimum-height-trees/

## Misc
- [ ] https://leetcode.com/problems/kth-largest-element-in-an-array/

# Questions sorted in order
Sorting these problems in a learning order can help you build up your skills progressively. I'll try to arrange them in a way that starts with simpler problems and gradually moves to more complex ones within each pattern. Here's how you can approach them:

### Foundational Concepts
1. [Two Sum](https://leetcode.com/problems/two-sum/) (Two Pointers)
2. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Sliding Window)
3. [Binary Search](https://leetcode.com/problems/binary-search/) (Modified Binary Search)
4. [Single Number](https://leetcode.com/problems/single-number/) (Bitwise XOR)
5. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (In-place Reversal of a LinkedList)
6. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Tree Breadth First Search)

### Sliding Window
1. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
2. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
3. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
4. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
5. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
6. [Permutation in String](https://leetcode.com/problems/permutation-in-string/)
7. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
8. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

### Two Pointers
1. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
2. [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
3. [3Sum](https://leetcode.com/problems/3sum/)
4. [3Sum Closest](https://leetcode.com/problems/3sum-closest/)
5. [Sort Colors](https://leetcode.com/problems/sort-colors/)
6. [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
7. [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

### Fast & Slow Pointers
1. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
2. [Happy Number](https://leetcode.com/problems/happy-number/)
3. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
4. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
5. [Reorder List](https://leetcode.com/problems/reorder-list/)

### Merge Intervals
1. [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
2. [Insert Interval](https://leetcode.com/problems/insert-interval/)
3. [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
4. [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

### Cyclic Sort
1. [Missing Number](https://leetcode.com/problems/missing-number/)
2. [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
3. [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

### In-place Reversal of a LinkedList
1. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
2. [Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
3. [Rotate List](https://leetcode.com/problems/rotate-list/)

### Tree Breadth First Search
1. [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
2. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
3. [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

### Tree Depth First Search
1. [Path Sum](https://leetcode.com/problems/path-sum/)
2. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
3. [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)
4. [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
5. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

### Two Heaps
1. [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
2. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
3. [IPO](https://leetcode.com/problems/ipo/)

### Subsets
1. [Subsets](https://leetcode.com/problems/subsets/)
2. [Subsets II](https://leetcode.com/problems/subsets-ii/)
3. [Permutations](https://leetcode.com/problems/permutations/)
4. [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

### Modified Binary Search
1. [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
2. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
3. [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)

### Bitwise XOR
1. [Single Number III](https://leetcode.com/problems/single-number-iii/)
2. [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)
3. [Flipping an Image](https://leetcode.com/problems/flipping-an-image/)

### Top 'K' Elements
1. [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)
2. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
3. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

### K-way Merge
1. [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
2. [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

### 0/1 Knapsack
1. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
2. [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)
3. [Target Sum](https://leetcode.com/problems/target-sum/)

### Topological Sort
1. [Course Schedule](https://

leetcode.com/problems/course-schedule/)
2. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
3. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

### Misc
1. [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

This should give you a structured way to tackle these problems. Good luck!
