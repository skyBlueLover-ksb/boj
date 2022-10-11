class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self, idx):
        node = self.head
        for i in range(idx):
            if node.next:
                node = node.next
            else:
                node = self.head
        return node

    def del_node(self, idx):
        if idx == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        node = self.get_node(idx-1)
        data = node.next.data
        node.next = node.next.next
        return data

N, K = map(int, input().split())
my_list = Linked_list(1)
for i in range(2, N+1):
    my_list.insert(i)
answer = []
idx = K-1
while my_list.head is not None:
    idx %= N
    answer.append(my_list.del_node(idx))
    idx += K-1
    N -= 1

print("<", end="")
for i in range(len(answer)-1):
    print(answer[i], end=", ")
print(answer[-1], end=">")
