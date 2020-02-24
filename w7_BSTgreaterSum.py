'''
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
'''
def bstToGst(root):
    '''
    right subtree -> root -> left subtree 순으로 방문하면 descending order로 element가 나온다. 그 앞까지의 sum을 더해주기만 하면 됨
    어떻게 다시 root를 찾아서 return 하는가? stack이 비어있으면 해당 변수 기억하기(while문 종료되기 직전 마지막 원소를 탐방할때도 스택이 비므로 이 경우와 구분해줘야) 이걸 원래 리스트에 append 후에 첫번째 element 반환하는 걸로 했다가 변수 None으로 initialize하는 것으로 소소하게 변경했는데 속도가 40.60에서 92.35로 올랐다. 이렇게 간단한건데 속도 차이가 크다니.

    O(n)/O(n)
    Runtime: 24 ms, faster than 92.35% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    '''
    stack, sum, ans = [], 0, None
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.right
        root = stack.pop()
        sum += root.val
        root.val = sum # copy?

        if not stack and not ans:
            ans = root

        root = root.left
        
    return ans

class Solution:
    '''
    Reversed inorder traversal in a Recursive Manner
    Recursive Manner의 좋은 점은 가장 먼저 시행하는 루트 단계의 환경이 끝까지 남아있기 때문에 iterative manner와 달리 반환하기 위해 root를 다시 찾아야하는 귀찮음이 없다.

    속도/메모리는 iterative 풀이와 동일하다
    Runtime: 24 ms, faster than 92.35% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    '''
    val = 0
    def bstToGst(self, root):
        if root.right: self.bstToGst(root.right) # right subtree로 self.val을 업데이트 한 뒤
        root.val = self.val = self.val + root.val # self.val과 root.val을 업데이트
        if root.left: self.bstToGst(root.left) # left subtree의 결과는 root 노드에 영향을 주지 않는다
        return root
    
