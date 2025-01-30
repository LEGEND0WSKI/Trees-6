# Time: O(n) traversal
# Space: O(n) queue/stack/recursion stack ;worst case
# Leetcode: Yes
# Issues: No

# bfs 15ms
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        q = deque()
        result = 0

        q.append(root)

        while q:
            curr = q.popleft()

            if low <= curr.val <= high:         # can be done pre, in and postorder trav
                result += curr.val

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        return result
    
# dfs 15 ms
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        self.helper(root,low,high)
        return self.result

    def helper(self, root, low, high):

        if not root: return

        if root.val >= low and root.val <= high:        # cond
            self.result += root.val

        self.helper(root.left,low,high)
        
        self.helper(root.right,low,high)

# usign 1 stack (dfs) 5ms
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        st = []

        result = 0

        while root or st:
            while root:
                st.append(root)
                root = root.left 
            root = st.pop()
            if low <= root.val <= high:
                result += root.val
            root = root.right

        return result
        