# Time: O(n)
# Space: O(n)
# Leetcode: Yes
# Issues: No


# bfs/ T:O(n)/ S:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root: return result

        hmap = defaultdict(list)

        q = deque()
        q.append(root)

        w = deque()
        w.append(0)

        mi = 0
        ma = 0
        while q:
            curr = q.popleft()              # queue 1 stores node
            currW = w.popleft()             # queue 2 stores position on numberline

            hmap[currW].append(curr.val)

            if curr.left:                   # if left child exists
                q.append(curr.left)
                w.append(currW-1)
                mi = min(mi, currW-1)
            
            if curr.right:                  # if right child exists
                q.append(curr.right)
                w.append(currW+1)
                ma = max(ma, currW+1)            
            

        for i in range(mi,ma+1):            # finally process hashmap
            result.append(hmap[i])

        return result
    
# dfs/ T:O(nlogk)/ S:O(n)
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root: return result      # empty
        self.hmap = defaultdict(list)
        self.mi = 0
        self.ma = 0

        self.dfs(root,0,0)

        for i in range(self.mi,self.ma+1):               # process hashmap after sorting on index location
            currList  = self.hmap[i]
            currList.sort(key = lambda x: x[1])
            result.append([x[0] for x in currList])
    
        return result

    def dfs(self,root,width,height):
        # base
        if not root: return

        self.mi = min(self.mi,width)
        self.ma = max(self.ma,width)

        self.hmap[width].append([root.val,height])  # store value and height to sort
        
        # logic
        self.dfs(root.left, width-1, height+1)
        self.dfs(root.right,width+1, height+1)
