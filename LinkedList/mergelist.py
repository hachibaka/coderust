from LinkedList_all import LinkedList, create_list

def merge_lists(l1, l2):
    newlist = LinkedList()
    node1 = l1.head
    node2 = l2.head

    while node1 and node2:
        if node1.value < node2.value:
            newlist.addNode(node1.value)
            node1 = node1.next
        elif node2.value < node1.value:
            newlist.addNode(node2.value)
            node2 = node2.next
        else:
            newlist.addNode(node1.value)
            newlist.addNode(node2.value)
            node1 = node1.next
            node2 = node2.next

    while node1:
        newlist.addNode(node1.value)
        node1 = node1.next

    while node2:
        newlist.addNode(node2.value)
        node2 = node2.next

    return newlist




l1 = create_list(100)
l2 = create_list(500)
print(l1)
print(l2)
newlist = merge_lists(l1, l2)
print(newlist)
