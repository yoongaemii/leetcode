'''
Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
'''
def rangeSumBST(root, L, R):
    '''
    search를 통해 L를 발견한다 -> R을 발견할 때까지 inorder traversal을 시행하며 sum에 더한다 
    * 굳이 inorder traversal까지 할 필요 없다? 방문하는 순서는 전혀 중요하지 않고 
    '''
    node, stack, rangeSum = root, [], 0

    # search L and construct stack for parents nodes of L
    while node.val != L:
        stack.append(node)
        if node.val > L:
            node = node.left
        elif node.val < L:
            node = node.right
    
    stack.append(node.right)
    # sum along inorder traversal
    while stack:
        while node:
            stack.append(node.right)

