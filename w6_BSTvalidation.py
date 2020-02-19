'''
validate Binary Search Tree
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
유의할 점은 각 노드에서 left < root < right 관계가 성립하더라도 BST가 아닐 수 있다는 점. left subtree의 '모든' element(grandchildren까지)가 root보다 작아야 하며, right subtree의 '모든' element가 root 보다 커야한다.
-> That means one should keep both upper and lower limits for each node while traversing the tree, and compare the node value not with children values but with these limits.
'''
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def isValidBST(root) -> bool:
    '''
    Basic Recursive
    left 노드로 이동할 때는 upper bound가 업데이트되고, right 노드로 이동할 때는 lower bound가 업데이트 된다
    recursive에서는 정말 작은 단계 씩 쪼개서 생각하는 게 중요한듯. 한 스텝에서 많이 하려고 하지 말고, 베이직 케이스를 작게 잡을 것(여기서는 leaf node를 베이스케이스로 잡을 수 있겠지만 루트부터 none일 경우를 감안해서 그냥 빈 노드가 들어가는 경우(리프노드에서 return helper를 불렀을 때)를 베이스 케이스로 잡았다.
    '''
    lower = float('-inf')
    upper = float('inf')

    def helper(node, lower, upper):
        if not node: return True
        # if node.left == None and node.right==None: return True 
        if lower < node.val and node.val < upper:
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
        return False

    return helper(root, lower, upper) 

root = TreeNode(2, left=TreeNode(1), right=TreeNode(5))
print(isValidBST(root))

def isValidBST(root):
    '''
    Recursive To Iterative with DFS
    stack에 노드와 그 노드의 lower bound, upper bound를 같이 저장한다.
    '''

def isValidBST(root):
    '''
    In-order Traversal: Left -> Node -> Right.
    BST에 대하여 inorder traversal을 진행하면 ascending order이기 때문에 다음 엘리먼트가 전보다 크지 않다면 invalidate
    솔루션을 보니 stack을 썼다. stack은 피치못하게 root노드(left, right이 아닌 중심노드)를 먼저 방문하게 되므로 쓸 수 없다고 생각했는데, 스택에 요소를 집어넣는 순서에 대해서 더 다양하게 생각해볼 수 있었다. DFS의 특성과 연관지어 생각해보면 '우선 왼쪽 끝까지 내려간다'고 생각하면 아이디어가 보인다.
    '''
    stack, inorder = [], float('-inf')
        
    while stack or root:
        while root: # 왼쪽으로 갈 수 있는데까지 (root.left가 None이 될때까지) 내려가기 / root가 없을때 즉, 리프노드에서 상위 while문이 끝난경우 stack에서 하나를 새로 꺼냄으로써 한 단계 위로 올라가기 
            stack.append(root)
            root = root.left
        root = stack.pop() # 지금 안 본 것 중에 크기가 가장 작아야하는 노드
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right # 리프노드에서는 None임

    return True
            
        