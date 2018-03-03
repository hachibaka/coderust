import random
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.lastnode = None

    def addNode(self,value):
        if not self.head:
            self.head = Node(value)
            self.lastnode = self.head
        else:
            self.lastnode.next = Node(value)
            self.lastnode = self.lastnode.next
        return self.head

    def reverse_list(self):
        if not self.head or not self.head.next :
            return self.head

        nextnode = self.head.next
        prevnode = self.head
        self.head.next = None
        i = 0
        while nextnode:
            temp = nextnode
            nextnode = nextnode.next
            temp.next = prevnode
            prevnode = temp
            i += 1
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

    def __len__(self):
        i = 0
        node = self.head
        while node:
            node = node.next
            i += 1

        return i

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

    def insertion_sort(self):
        sortednode = None
        node = self.head
        while node:
            nextnode = node.next
            if not sortednode:
                sortednode = node
                sortednode.next = None
            elif node.value <= sortednode.value:
                node.next = sortednode
                sortednode = node
            else:
                tempnode = sortednode
                prevnode = None
                while tempnode and tempnode.value < node.value:
                    prevnode = tempnode
                    tempnode = tempnode.next
                prevnode.next = node
                node.next = tempnode
            node = nextnode
        self.head = sortednode

    def __str__(self):
        node = self.head
        output = []
        i = 0
        while node:
            output.append(node.value)
            node = node.next
        return "length of linkedlist is " + str(len(output)) + "\n"+ '-->'.join(map(str,output))

linkedlist1 = LinkedList()
for _ in range(20):
    linkedlist1.addNode(random.randint(-100,100))

linkedlist1.removeduplicates()
#linkedlist.deleteNode(34)
#linkedlist.deletefromlast(34)
#linkedlist.reverse_list()
#print(linkedlist)
linkedlist1.insertion_sort()
print(linkedlist1)


linkedlist2 = LinkedList()
for _ in range(20):
    linkedlist2.addNode(random.randint(-100,100))

linkedlist2.removeduplicates()
#linkedlist.deleteNode(34)
#linkedlist.deletefromlast(34)
#linkedlist.reverse_list()
#print(linkedlist)
linkedlist2.insertion_sort()
print(linkedlist2,len(linkedlist2))

def intersect(l1, l2):
    if not l1.head or not l2.head:
        return None
    match = None
    m, n = len(l1), len(l2)
    i = j = 0
    pass
