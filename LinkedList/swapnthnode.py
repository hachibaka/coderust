from LinkedList_all import LinkedList, create_list

def swapnthnode(ll,n):
    i = 0
    node = ll.head
    prev_node = None
    while node and i < n-1:
        prev_node = node
        node = node.next
        i += 1

    if i!= n - 1:
        return ll.head
    else:
        prev_node.next = ll.head
        temp = ll.head.next
        ll.head.next = node.next
        node.next = temp
        ll.head = node

        return node

linkedlist1 = create_list(20)
print(linkedlist1)
node = swapnthnode(linkedlist1,2)
print(node.value)
print(linkedlist1)
