from buildtree import BinaryTree

class InorderIterator:
    def __init__(self,root):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return True if self.stack else False

    def getNext(self):
        if not self.stack:
            return None
        r_val = self.stack.pop()
        temp = r_val.right
        while temp:
            self.stack.append(temp)
            temp = temp.left

        return r_val.data

    def __iter__(self):
        return self

    def __next__(self):
        if not self.hasNext():
            raise StopIteration
        else:
            return self.getNext()

def inorder_iterative(root):
    if not root:
        return None

    stack = []
    while stack or root:
        print(",".join(str(node.data) for node in stack))
        if root:
            stack.append(root)
            root = root.left
            continue
        popnode = stack.pop()
        #print(popnode.data,end=", ")
        root = popnode.right


if __name__ == "__main__":
    btree = BinaryTree()
    values = [100,30,40,60,20,10,90,125,200,114]
    for value in values:
        btree.insert(value)
    print(btree)
    print("Printing Inorder of Tree using Iterator")
    for nodevalue in InorderIterator(btree.root):
        print(nodevalue,sep="",end=", ")
    print()
    print("Printing Inorder of Tree using Iterative method")
    inorder_iterative(btree.root)
