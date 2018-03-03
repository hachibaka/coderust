import random
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def addNode(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            node = self.head
            while node:
                if not node.next:
                    break
                else:
                    node = node.next
            node.next = Node(value)
        return self.head

    def reverse_list(self):
        if not self.head or not self.head.next :
            return self.head

        nextnode = self.head.next
        prevnode = self.head

        while nextnode:
            temp = nextnode
            nextnode = nextnode.next
            temp.next = prevnode
            prevnode = temp
        self.head = prevnode
        return self.head

    def deleteNode(self, key):
        node = self.head
        prev_node = None
        while node:
            if node.value == key:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
        return self.head

    def removeduplicates(self):
        dups = []
        node = self.head
        prev_node = None
        while node:
            if node.value in dups:
                prev_node.next = node.next
            else:
                dups.append(node.value)
            prev_node = node
            node = node.next
        return self.head

    def deletefromlast(self, key):
        deletenode = None
        node = self.head
        while node:
            if node.value == key:
                deletenode = node
            node = node.next

        if not deletenode:
            return self.head

        prev_node = None
        node = self.head
        while node:
            if node == deletenode:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
        return self.head

    def __str__(self):
        node = self.head
        output = []
        while node:
            output.append(node.value)
            node = node.next
        return '-->'.join(map(str,output))

linkedlist = LinkedList()
for _ in range(17):
    linkedlist.addNode(random.randint(-100,100))
print(linkedlist)
#linkedlist.removeduplicates()
#linkedlist.deleteNode(34)
linkedlist.deletefromlast(34)

print(linkedlist)
linkedlist.reverse_list()
print(linkedlist)
