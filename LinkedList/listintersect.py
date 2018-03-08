from LinkedList_all import LinkedList, create_list

def intersect(l1, l2):
    if not l1.head or not l2.head:
        return None
    match = None
    m, n = len(l1), len(l2)
    i = j = 0
    node1 = l1.head
    node2 = l2.head
    newlist = None
    while node1 and node2:
        if node1.value == node2.value:
            if not newlist:
                newlist = LinkedList()
            newlist.addNode(node1.value)
            node1 = node1.next
            node2 = node2.next
        elif node1.value > node2.value:
            node2 = node2.next
        else:
            node1 = node1.next
    return newlist

l1 = create_list(10000)
l2 = create_list(10000)
print(l1)
print(l2)
newlist = intersect(l1,l2)
print(newlist)
