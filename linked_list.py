class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printll(self):
        cur_node = self.head
        print("\nLinked list is")
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_betwn(self, prev, data):
        
        new_node = Node(data)

        pr_node = self.head
        while pr_node.next:
            if prev is pr_node.data:
                new_node.next = pr_node.next
                pr_node.next = new_node
                break

            elif prev is not pr_node.data:
                pr_node = pr_node.next

            else:
                print("previous element not in linkedlist")



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("E")
node = input("Enter the node after which you want to add a new node: ")
data = input("Enter new node: ")
llist.insert_betwn(node,data)
llist.printll()
print("\n")