'''
Cherry Pickup
https://leetcode.com/problems/cherry-pickup/
#Dynamic_Programming #Hard

In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:
- grid is an N by N 2D array, with 1 <= N <= 50.
- Each grid[i][j] is an integer in the set {-1, 0, 1}.
- It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
'''

grid = [[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]

cherry = 0 # 현재 가지고 있는 체리 수
curr = [0,0] # 현재 말의 위치
way = 0 # 가는 중인지 오는 중인지
output = 0

# TODO: 어떻게 해야 backtrack을 쓰면서도 stack이 비어야 종료되도록 할 수 있을까?
def backtrack(candidate):
    if way==1 and candidate==[0,0]:
        output = max(output, cherry)
        return # 그러면 최대값을 어떻게 찾지?
    
    # iterate all possible candidates.
    for next_candidate in generate_candidates(way):
        if next_candidate != -1: # TODO: candidate를 방향으로 해놓고 visit에서 말 옮기는 것을 처리하면 if문에서는 어떻게 -1을 판단할까?
            visit(next_candidate)
            backtrack(next_candidate)
            remove(next_candidate)

def R(curr):
    return [curr[0], curr[1]+1]

def D(curr):
    return [curr[0]+1, curr[1]]

def L(curr):
    return [curr[0], curr[1]-1]

def U(curr):
    return [curr[0]-1, curr[1]]

inverse = {R:U, U:R, D:U, U:D}

def generate_candidates(way):
    return [R, D] if way == 0 else [L, U]

def visit(candidate):
    curr = candidate(curr)
    if grid[curr[0]][curr[1]] == 1:
        cherry +=1
    if curr == [n-1, n-1]:
        way = 1

def remove(candidate):
    if grid[curr[0]][curr[1]] == 1:
        cherry -=1
    if curr == [n-1, n-1]:
        way = 0
    curr = inverse[candidate](curr)
