'''
Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
'''
def rangeSumBST(root, L, R):
    '''
    search를 통해 L를 발견한다 -> R을 발견할 때까지 inorder traversal을 시행하며 sum에 더한다 
    * 굳이 inorder traversal까지 할 필요 없다? 방문하는 순서가 중요한게 아니라 합만 내면 되잖아
    '''
    node, stack, res = root, [], 0

    # search L and construct stack for parents nodes of L
    while node.val != L:
        stack.append(node)
        if node.val > L:
            node = node.left
        elif node.val < L:
            node = node.right
    
    res += node.val

    # add right subtree of the L node

    # find the node to start inorder traversal
    while node.val <= L:
        node = stack.pop()
    
