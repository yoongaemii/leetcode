'''
Level Order Traversal 
https://leetcode.com/problems/binary-tree-level-order-traversal/
빈 공간에는 None을 집어 넣으며 다음 레벨로 넘어가기 쉽지 않을까 했는데 비대칭적인 tree의 경우 극심한 공간 비효율성 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    '''
    O(n)/O(n)
    큐에 자녀 노드들을 넣되, 레벨을 같이 넣어서 리스트 내에 서브리스트로 구분되게 하는 방법
    '''
    q = deque()
    if root:
        q.append((root, 0))
    output = defaultdict(list)

    while q:
        r, level = q.popleft()
        output[level].append(r.val)
        if r.left:
            q.append((r.left, level+1))
        if r.right:
            q.append((r.right, level+1))
        
    return list(output.values())

'''
Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''

# 방문하는 노드가 아니라 자녀노드를 output에 넣고(지시된 순서대로) q에 넣는 순서는 또 다르다면?
    # if r[1] % 2 == 0:
    #     output[r[1]+1].extend([r[0].right.val, r[1].left.val])   # output에 자녀노드 거꾸로 입력하기    
    #     q.extend([(r[0].left, r[1]+1), (r[0].right, r[1]+1)])  # q에 자녀노드 제대로 입력하기

    # else:
    #     output[r[1]+1].extend([r[0].left.val, r[1].right.val]) # output에 자녀노드 제대로 입력하기    
    #     q.extend([(r[0].left, r[1]+1), (r[0].right, r[1]+1)]) # 이렇게 안된다ㅜㅜㅜㅜ

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    '''
    levelOrder Traversal을 시행한 뒤 순서만 바꾸는 방법: O(n)/?
    Runtime: 32 ms, faster than 55.88% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    '''
    out = self.levelOrder(root)
    return [sublist if i%2==0 else sublist[::-1] for i, sublist in enumerate(out)] 

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    '''
    BFS: 어떻게 다음 레벨인지 알지? 두번째 레벨의 노드들은 같이 append 된다
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS
    '''
    if not root: return []
    res, temp, q, flag=[], [], [root], 1
    while q:
        for _ in range(len(q)): # 이 순간에 q 안에 있는 노드만 돌도록
            node = q.popleft()
            temp.append(node)
            if node.left: q += [node.left]
            if node.right: q += [node.right]
        res+=[temp[::flag]]
        temp=[]
        flag*=-1
    return res
            
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    '''
    Recursion
    depth에 따라 앞에 붙이냐, 뒤에 붙이냐를 달리 한다
    호출 순서를 보면 왼쪽까지 최대한 내려갔다가 거슬러 올라오며 오른쪽 엣지를 타기 때문에 같은 레벨에 대해서는 왼쪽부터 오른쪽 노드 순서대로 traversal함수가 호출된다
    '''
    ans = [[]]
    def traversal(curr, depth):
        if len(ans) == depth: ans.append([])
        if not curr: return
        ans[depth] = [curr.val] + ans[depth] if depth % 2 else ans[depth] + [curr.val]
        if curr.left:traversal(curr.left, depth + 1)
        if curr.right:traversal(curr.right, depth + 1)
    traversal(root, 0)
    return root and ans