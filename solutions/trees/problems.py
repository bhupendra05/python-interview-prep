"""
Trees & Binary Search Trees — Interview Problems
=================================================
BFS, DFS, recursion, and BST property problems.
"""
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, vals: list) -> Optional["TreeNode"]:
        """Build a tree from level-order list (None = missing node)."""
        if not vals:
            return None
        root = cls(vals[0])
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            node = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = cls(vals[i])
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = cls(vals[i])
                queue.append(node.right)
            i += 1
        return root


# ─────────────────────────────────────────────────────────────────────────────
# 1. Maximum Depth of Binary Tree
# Time: O(n)  Space: O(h) h = tree height
# ─────────────────────────────────────────────────────────────────────────────
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ─────────────────────────────────────────────────────────────────────────────
# 2. Invert Binary Tree
# Time: O(n)  Space: O(h)
# ─────────────────────────────────────────────────────────────────────────────
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ─────────────────────────────────────────────────────────────────────────────
# 3. Diameter of Binary Tree
# Longest path between any two nodes (may not pass through root).
# Time: O(n)  Space: O(h)
# ─────────────────────────────────────────────────────────────────────────────
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter


# ─────────────────────────────────────────────────────────────────────────────
# 4. Balanced Binary Tree
# Determine if tree is height-balanced (depth of any two subtrees ≤ 1).
# Time: O(n)  Space: O(h)
# ─────────────────────────────────────────────────────────────────────────────
def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


# ─────────────────────────────────────────────────────────────────────────────
# 5. Same Tree
# Time: O(n)  Space: O(h)
# ─────────────────────────────────────────────────────────────────────────────
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# ─────────────────────────────────────────────────────────────────────────────
# 6. Level Order Traversal (BFS)
# Time: O(n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 7. Lowest Common Ancestor of BST
# Time: O(h)  Space: O(1)
# ─────────────────────────────────────────────────────────────────────────────
def lca_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
    return root


# ─────────────────────────────────────────────────────────────────────────────
# 8. Binary Tree Right Side View
# Return the values visible from the right side (rightmost at each level).
# Time: O(n)  Space: O(n)
# ─────────────────────────────────────────────────────────────────────────────
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:  # rightmost at this level (reverse BFS trick)
                result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return result


# ─────────────────────────────────────────────────────────────────────────────
# 9. Validate Binary Search Tree
# Time: O(n)  Space: O(h)
# ─────────────────────────────────────────────────────────────────────────────
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    return validate(root, float('-inf'), float('inf'))


# ─────────────────────────────────────────────────────────────────────────────
# 10. Serialize and Deserialize Binary Tree
# Encode tree to string and decode it back.
# ─────────────────────────────────────────────────────────────────────────────
def serialize(root: Optional[TreeNode]) -> str:
    result = []
    def dfs(node):
        if not node:
            result.append('N')
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ','.join(result)


def deserialize(data: str) -> Optional[TreeNode]:
    vals = iter(data.split(','))
    def dfs():
        val = next(vals)
        if val == 'N':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
