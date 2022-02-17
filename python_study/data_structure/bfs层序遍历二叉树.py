from collection import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 给定二叉树：[3,9,20,null,null,15,7]
def bfs(root: TreeNode):
    if not root:
        return []

    res = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            res.append(node.left)
        if node.right:
            res.append(node.right)



