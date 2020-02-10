'''
Permutations
https://leetcode.com/problems/permutations/
#Backtracking

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

'''
python itertools의 permutations: `itertools.permutations([1,2,3])`
Runtime: 44 ms, faster than 25.30% of Python3 online submissions for Permutations.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations.
'''

'''
Python names and list contents are references, and unless documented otherwise, no copies are created when you pass a name to a method. This applies just as much to list.append() as to any other call; list.append() adds a reference to the list, not a copy
'''


def permute(nums):
    '''
    backtracking을 활용해 한 자리 씩 완성해 나가는 방법. 각 자리수가 정해진 후 그 이하 자릿수의 모든 가능성을 탐색하고 돌아와야하기 때문에 backtracking을 사용했다.
    Runtime: 40 ms, faster than 58.89% of Python3 online submissions for Permutations.
    Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutations.
    '''
    output = []
    curr =[]

    def backtrack(candidate):
        # 여기 trial이 들어가는 게 아니고?

        if len(nums) <= 1: 
            curr.extend(nums)
            output.append(curr.copy())
            del curr[-1]
            return
        
        # iterate all possible candidates.
        for next_candidate in set(nums):
                
            # try this partial candidate solution
            place(next_candidate)
            
            # given the candidate, explore further.
            backtrack(next_candidate) 
            
            # 앞선 시도를 되돌리기
            if len(curr) >= 1: nums.append(curr.pop()) 

    def place(candidate):
        curr.append(candidate)
        nums.remove(candidate)

    # for i in set(nums):
    #     place(i)
    #     backtrack(i)
    #     if len(curr) >= 1: nums.append(curr.pop()) 

    backtrack()
    return output



def permute(nums):
    '''
    Decrease and Conquer in a Recursive Method를 제대로 구현하지 못했다....
    copy를 반환했는데 왜 permute를 호출할때는 다시 원래 nums가 되어있니!!!????
    '''
    if len(nums) <= 1:
        return [nums] # list of list

    else:
        return [[n].extend(sub) for n in set(nums) for sub in permute(inlineRemove(nums, n))]

def inlineRemove(seq, ele):
    copy = seq.copy()
    copy.remove(ele)
    return copy #여기에 permute()을 적용하고 싶은건데!!!!????

def permute(nums):
    '''
    Decrease and Conquer in an Iterative Manner - backtracking 보다 런타임 개선
    Runtime: 48 ms, faster than 17.05% of Python3 online submissions for Permutations.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations.
    '''
    if len(nums) <= 1:
        return [nums]

    stack = [[s, len(nums)] for s in set(nums)]
    output = []
    item = []
    while True: 
        if len(nums) <= 0:
            output.append(item)
            if stack:
                i = stack[-1][1] # 어디까지 지워야 하나?
                nums.extend(item[-i:].copy())
                item = item[:-i]
            else: break

        else:
            curr = stack.pop()
            item.append(curr[0]) 
            nums.remove(curr[0])
            stack.extend([[s,len(nums)] for s in set(nums)]) # 스택에 자릿수를 표시함. 뒤에서 몇번째 자리수에 갈 놈인가?

    return output

nums = [1,2]
print(permute(nums))