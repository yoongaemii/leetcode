'''
Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''

def maxPathSum(root):
    '''
    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39775/Accepted-short-solution-in-Java
    subtree의 정보를 활용해서 root에서 수합/판단하는 Bottom up approach
    recursive한 설계이지만 root를 지나는 path를 완성시키는 combine과정과 별개로 중간중간 정답값인 maxval을 업데이트하는 과정이 있다.
    인상깊었던 트릭은 maxPathDown의 결과를 0과 비교하여 노드를 탈락시키는 것. max(left, right)과 함께 원하는 효과를 낸다.
    
    Runtime: 92 ms, faster than 59.37% of Python3 online submissions for Binary Tree Maximum Path Sum.
    Memory Usage: 19.5 MB, less than 100.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
    '''
    maxval = float('-inf')
    maxPathDown(root)
    return maxval

def maxPathDown(node):
    if not node: return 0

    # 노드를 마주쳤을 때, 앞선 path에서 이어지는 것을 택할것인가 아니면 자녀들을 활용해 새로운 path를 구축할 것을 택할것인가?
    # right 노드를 더할 것인가? -> right으로 쭉 이었을 때 얼마나 큰 sum 구축 가능? 0 미만이면 (left보다 커도) 그냥 버리는 게 낫다
    left = max(0, maxPathDown(node.left))
    right = max(0, maxPathDown(node.right))

    # 지금의 노드와 자녀들을 지나가는 path의 sum.
    maxval = max(maxval, node.val + left + right) 
    # 기존 루트와 이어지는 path도 계산하기 위한 리턴값
    return node.val + max(left, right)
