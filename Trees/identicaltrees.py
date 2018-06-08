from buildtree import BinaryTree


def check_identical(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and not root2:
        return False
    if root2 and not root1:
        return False
    return ( root1.data == root2.data and
    check_identical(root1.left, root2.left) and
    check_identical(root1.right, root2.right))


if __name__ == "__main__":
    btree1 = BinaryTree()
    btree2 = BinaryTree()

    values = [100,30,40,60,20,10,90]
    for value in values:
        btree1.insert(value)
        btree2.insert(value)
    print("************Printing Btree 1")
    print(btree1)
    print("************Printing Btree 2")
    print(btree2)
    print("Are both trees identical ?",check_identical(btree1.root, btree2.root))
