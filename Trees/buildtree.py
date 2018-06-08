from collections import deque
import random
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.level = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,newvalue):
        if not self.root:
            self.root = TreeNode(newvalue)
        else:
            prev_node = None
            tempnode = self.root
            left = right = False
            level = 0
            while tempnode:
                prev_node = tempnode
                level += 1
                if newvalue <= tempnode.value:
                    tempnode = tempnode.left

                    left = True
                    right = False
                else:
                    tempnode = tempnode.right

                    left = False
                    right = True
            newnode = TreeNode(newvalue)
            if left:
                prev_node.left = newnode
                newnode.level = level
            else:
                prev_node.right = newnode
                newnode.level = level

    def __str__(self):
        #Printing Binary Node
        output = []
        queue = deque()

        node = self.root
        queue.append(node)

        treelevel = {}

        while queue:
            node = queue.popleft()
            if node.level in treelevel:
                treelevel[node.level].append(node.value)
            else:
                treelevel[node.level] = [node.value]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        maxlevel = max(treelevel.keys())
        for i in range(maxlevel+1):
            output.append("-->".join(map(str,treelevel[i])))
        return "\n".join(output)

btree = BinaryTree()
for _ in range(20):
    btree.insert(random.randint(1,100))
print(btree)
