from LinkedList_all import LinkedList, create_list

def findnthnode(l1,n):
    head = tail = l1.head
    i = 0
    while tail and i < n:
        tail = tail.next
        i += 1
    if i != n:
        return None
    if not tail:
        return head

    while tail:
        head = head.next
        tail = tail.next

    return head

l1 = create_list(10)
l2 = create_list(5)
print(l1)
print(l2)
node = findnthnode(l1,5)
if node: print(node.value)
node = findnthnode(l1,3)
if node :print(node.value)

node = findnthnode(l2,5)
if node: print(node.value)
node = findnthnode(l2,0)
if node : print(node.value)
