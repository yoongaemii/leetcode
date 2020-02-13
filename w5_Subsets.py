'''
Subsets
https://leetcode.com/problems/subsets/
#Dynamic_Programming

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

nums = [1,2,3]
def subsets(nums):
    '''
    Runtime: 32 ms, faster than 68.36% of Python3 online submissions for Subsets.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subsets.
    '''
    dp = [[]]
    for i in nums:
        dp.extend([subset+[i] for subset in dp])
    return [list(s) for s in set(tuple(i) for i in dp)]
