'''
Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
'''
def rightSideView(root):
    '''
    BFS using the same 'for _ in range(len(q))' trick in Zigzag. O(n)/O(n)
    Runtime: 28 ms, faster than 82.25% of Python3 online submissions for Binary Tree Right Side View.
    Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Right Side View.
    '''
    if not root: return []
    q = [root]
    res = []

    while q:
        for _ in range(len(q)):
            node = q.pop(0)
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
        res.append(node.val) # the last and rightmost node at current level

    return res


def rightSideView(self, root):
    '''
    iterative, level-by-level
    위 BFS와 동일한 풀이인데 q를 계속 이어서 쓰는 것이 아니라 level이라는 리스트를 말그대로 레벨마다 새로 할당하여 읽기에 더 직관적.
    '''
    ans,level=[],[root]
    while root and level:
        ans.append(level[-1].val)
        level=[k for n in level for k in (n.left,n.right) if k]
    return ans

def rightSideView(self, root):
    '''
    Recursive, combine right and left
    Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be O(n^2), though.
    '''
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):] # root에 right subtree에서 나온 뷰를 더하고 left subtree가 더 길다면 이를 활용해 뒷부분을 채워준다



'''
Python Dictionary Trick
.setdefault(key, value)는 해당 key의 value를 고정한다. 이 문제에서처럼 오른쪽 뷰를 저장한 다음에 오른쪽에 없던 레벨이었을 때만 딕셔너리를 업데이트 하고자 한다면 효과적
'''
rightmost_value_at_depth = dict() # depth -> node.val
rightmost_value_at_depth.setdefault(depth, node.val)

