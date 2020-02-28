'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
root만 반환한다 해도 .right 와 .left로 연결관계 정보가 포함되기 때문에 실제로 지워야한다!
'''


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root, to_delete):
        '''
        초기 풀이의 문제점
        1.
        클래스 함수 delNodes 내에서 forest라는 변수를 초기화하고 이를 BFS라는 함수를 호출하며 변경하고 싶은데 UnboundLocalError: local variable 'forest' referenced before assignment 가 뜬다. 클래스변수로 선언하면 self.forest를 통해 원하는대로 작동시킬 수 있으나 [root]로 초기화할 수 없다. -> 클래스 함수 안에 self.forest=[root]
        2. 노드가 업데이트 되지 않는다
        root=None으로 하는 것만으로는 안된다. root라는 변수가 left혹은 right의 주소를 가져오는 게 아니라 값을 가져오기 때문에. 
        방향을 바꿔서 to_delete를 자식노드로 가지고 있는 부모의 입장에서 생각해보자
        '''
        self.forest = [root]
        def BFS(root):
            if root == None:
                return

            BFS(root.left)
            BFS(root.right)
            
            if root.val in to_delete:
                if root in self.forest: self.forest.remove(root)
                self.forest += [node for node in [root.left, root.right] if node]
                root=None

        BFS(root)
        return self.forest


class Solution:
    '''
    left와 right를 삭제해야하기 때문에 to_delete 포함 여부를 부모측에서 판단하는 게 쉽다 vs 부모 자식 간 연달아 to_delete 포함일 수 있으므로 본인 측에서 판단하는 게 쉽다
    --> 부모 측에서 판단하고 새로운 root 시작할 때 to_delete 포함 여부 판단하는 것으로 설계

    Runtime: 84 ms, faster than 19.41% of Python3 online submissions for Delete Nodes And Return Forest.
    Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Delete Nodes And Return Forest.
    '''
    def delNodes(self, root, to_delete):
        queue = [root] if root else []
        roots = []

        while queue: 
            root = queue.pop(0)
            if root.val in to_delete: # 부모-자식 to_delete가 연달아 나오는 경우
                queue += [child for child in [root.left, root.right] if child]
                continue 
            else:
                roots.append(root)

            stack = [root]
            while stack:
                node = stack.pop()
                if node.left:
                    if node.left.val in to_delete: 
                        if node.left.left: queue.append(node.left.left)
                        if node.left.right: queue.append(node.left.right)
                        node.left = None
                    else: stack.append(node.left)
                if node.right:
                    if node.right.val in to_delete: 
                        if node.right.left: queue.append(node.right.left)
                        if node.right.right: queue.append(node.right.right)
                        node.right = None
                    else: stack.append(node.right)
        print(roots)
        return roots

root = TreeNode(1, TreeNode(2), TreeNode(3,right=TreeNode(4)))
s = Solution()
s.delNodes(root, [2,1])
