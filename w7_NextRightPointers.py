'''
Populating Next Right Pointers in Each Node

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Trial 1: level order traversal 하듯이 현 레벨에서 넥스트 레벨의 노드 리스트를 구축한 뒤 for 문을 돌며 .next를 할당하는 방법을 생각해봤지만 넥스트 레벨의 노드 리스트는 O(n)의 extra space를 사용한다.

'''
class Solution:
    '''
    level order traversal 하듯이 현 레벨에서 넥스트 레벨의 노드 리스트를 구축한 뒤 for 문을 돌며 .next를 할당하는 방법. 
    TODO: 함수의 arguement로 넘기면 implicit stack space를 활용하게 된다?

    Runtime: 64 ms, faster than 65.30% of Python3 online submissions for Populating Next Right Pointers in Each Node.
    Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.
    '''
    def connect(self, root):
        if root: self.traverse([root])
        return root
        
    def traverse(self, level):
        for i in range(len(level)):
            try:
                level[i].next = level[i+1]
            except IndexError: # end of the level. keep as null
                pass 
            except AttributeError: # we are beyond leaf nodes
                return 

        return self.traverse([child for node in level for child in [node.left, node.right]]) # extra space?
        


class Solution:
    '''
    서미지님 풀이
    부모 측에서 자녀노드들의 next를 지정해주며, subtree를 넘나들며 next를 설정해줘야하는 문제는 root.next를 통해 해결한다. recursive에서 중요한 것은 그 전 단계가 모두 해결되어있다고 생각한는 것. 이 문제에서 그 전 단계가 해결되어있다는 것은 2에서 자신의 오른쪽 sibling에 바로 접근할 수 있다는 점이다. 
    '''
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                self.connect(root.left)
                self.connect(root.right)

        return root
