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
    return [list(s) for s in set(tuple(i) for i in dp)] # 이거 안해도 됨 distinct integers라고 되어있음


'''
TODO: 풀이 확인해보기
어떤 요소가 '있다/없다'를 생각해서 recursive 혹은 backtracking으로 풀 수 있다
'''

'''
허정민님/류원탁님 bitmask 풀이
숫자가 세 개 있다면 세자리 이진수로 가능한 모든 수. 001 이라면 이걸 bitmask로 써서 3이 나온다!
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, N = [], len(nums)
        for i in range(2 ** N, 2 ** (N+1)):
            bitmask = bin(i)[3:]
            ans.append([nums[i] for i, b in enumerate(bitmask) if b == '1'])
        return ans