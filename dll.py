class Node:
    # constructor to create a new node
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev


# class Linked List
class LinkedList:
    # constructor to create an empty LinkedList
    def __init__(self):
        self.head = None

class DoublyLinkedList:
    class Node:
        # constructor to create a new node
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data, prev=node)
            node.next = new_node
            self.tail = new_node

    def delete_node(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def delete_data(self, data):
        node = self.head
        while node.data != data:
            node = node.next

        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

my_dll = DoublyLinkedList(1)


