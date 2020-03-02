'''
Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
#Medium #BFS #DFS #Topological_Sort #Graph
'''
from typing import List
from collections import defaultdict

class Solution:
    '''
    75분 소요
    Runtime: 264 ms, faster than 7.83% of Python3 online submissions for Course Schedule II.
    Memory Usage: 18.8 MB, less than 7.14% of Python3 online submissions for Course Schedule II.

    1. 그 전 노드로 되돌아오기: 보스를 ans에 더할 수 있는 만큼 더한 뒤 outgoing adj가 더 없는 곳에서 되돌아와야 하는데 이를 처리하기가 곤혹스러웠다. visitied와 별개의 데이터를 써볼까 했는데 adjacent nodes에 대해 for 문을 돈 뒤에 append를 하는 것으로. recursive call로 함수를 끝내는 것 밖에 못했는데 그래도 발전이 있었다!
    1-1. prerequisites를 dictionary로 변환하지 말고 그대로 써볼까도 했다. 양쪽에서 접근할 수 있도록
    2. acyclic 여부의 판단 시점과 return 시점 분리하기: 함수 내부에 isAcyclic 변수를 선언하고 이를 append 이후에 반환하는 것으로. 한 함수 내에서 append와 isAcyclic 여부 판단이 섞여 있는데 이를 분리할 수 있다면 좋을 듯
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_dict = defaultdict(list)
        for adj, node in prerequisites:
            adj_dict[node].append(adj)

        visited = [0] * numCourses
        ans = []

        def add_boss_return_isAcyclic(i):
            if i in ans: return True
            if visited[i]: return False # cyclic: ans에는 없지만 visited에 있는 상태는 지금 붙이면 안된다는 뜻이다

            visited[i] = 1
            isAcyclic = [add_boss_return_isAcyclic(adj) for adj in adj_dict[i]] # 안에서 전역변수를 바꾼다는 사실을 알아보기 힘들지 않나? 
            ans.append(i)      

            return all(isAcyclic) # cf) all([]) == True
        
        if all([add_boss_return_isAcyclic(i) for i in range(numCourses)]):
            return ans[::-1]
        else:
            return []


s = Solution()
print(s.findOrder(4, [[1,0],[0,2]]))

def findOrder(self, numCourses, prerequisites):
    '''
    https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.

    1. incoming node가 없는 노드들만 stack에 넣어 탐색의 시작점으로 삼음으로써 가짓수를 줄였다.
    2. 답을 구축할 때 시간 순서대로 하는데, 내가 가리키는 노드들의 incoming node에서 자기 자신을 제거하며, incoming node가 그런식으로 모두 제거되어있을 때만 stack에 넣어 다음 append 후보로 처리하는 방식.
    '''
    dic = collections.defaultdict(set)
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j) # i를 가리키는 노드 
        neigh[j].add(i) # j가 가리키는 노드 
    stack = [i for i in xrange(numCourses) if not dic[i]] 
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]: # incoming 노드가 모두 res에 들어가 있으면 탐색 가능 
                stack.append(i)
        dic.pop(node) # outgoing 노드들을 모두 처리한 뒤에 dictionary에서 제거
    return res if not dic else []