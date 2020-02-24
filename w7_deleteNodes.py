'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
root만 반환한다 해도 .right 와 .left로 연결관계 정보가 포함되기 때문에 실제로 지워야한다!
'''
'''
클래스 함수 delNodes 내에서 forest라는 변수를 초기화하고 이를 BFS라는 함수를 호출하며 변경하고 싶은데 UnboundLocalError: local variable 'forest' referenced before assignment 가 뜬다. 클래스변수로 선언하면 self.forest를 통해 원하는대로 작동시킬 수 있으나 [root]로 초기화할 수 없다.
'''
class Solution:
    forest = []
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # forest = [root]
        def BFS(root):
            if root == None:
                return
            if root.val in to_delete:
                if root in self.forest: self.forest.remove(root)
                self.forest += [node for node in [root.left, root.right] if node]
            
            BFS(root.left)
            BFS(root.right)

        BFS(root)
        return self.forest + [root]