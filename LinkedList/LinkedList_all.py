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

    def split_lists(self,headnode):
        pass

    def split_half(self,first_second):
        if not self.head:
            first_second.first = None
            first_second.second = None
            return  

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head
        first_second = pair()

        return sortednode

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

def create_list(n):
    linkedlist = LinkedList()
    for _ in range(n):
        linkedlist.addNode(random.randint(-500,500))
    linkedlist.removeduplicates()
    linkedlist.insertion_sort()
    return linkedlist

if __name__ == '__main__':

    linkedlist1 = create_list(200)
    linkedlist2 = create_list(200)
    print(linkedlist1)
    print(linkedlist2)
