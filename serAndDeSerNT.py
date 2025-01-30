# Time: O(n)
# Space: O(n); for dfs :recursion stack additional overhead
# Leetcode: Yes
# Issues: No

# bfs 91 ms
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        sb = ""

        def dfsSer(root):
            nonlocal sb
            #base
            if not root:
                sb += '#'
                sb += ','                
                return 

            #logic
            sb += str(root.val)
            sb += ','

            dfsSer(root.left)
            dfsSer(root.right)

        dfsSer(root)
        # print(sb)
        return sb
       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)== 0: return None

        splitArr = data.split(',')
        idx = 0

        def dfsDes(splitArr):
            nonlocal idx
            #basecase
            if splitArr[idx] == '#':
                idx +=1
                return None

            #logic
            root = TreeNode(int(splitArr[idx]))
            idx += 1
            
            root.left = dfsDes(splitArr)
            root.right = dfsDes(splitArr)

            return root
        return dfsDes(splitArr)


# dfs 110 ms
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        sb = ""

        def dfsSer(root):
            nonlocal sb
            #base
            if not root:
                sb += '#'
                sb += ','                
                return 

            #logic
            sb += str(root.val)
            sb += ','

            dfsSer(root.left)
            dfsSer(root.right)

        dfsSer(root)
        # print(sb)
        return sb
       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)== 0: return None

        splitArr = data.split(',')
        idx = 0

        def dfsDes(splitArr):
            nonlocal idx
            #basecase
            if splitArr[idx] == '#':
                idx +=1
                return None

            #logic
            root = TreeNode(int(splitArr[idx]))
            idx += 1
            
            root.left = dfsDes(splitArr)
            root.right = dfsDes(splitArr)

            return root
        return dfsDes(splitArr)
