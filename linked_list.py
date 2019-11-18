class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def printll(self):
        lenl = 0
        cur_node = self.head
        if cur_node == None:
            print("\nLinked list is Empty")

        else:
            
            print("\nLinked list is")
            while cur_node:
                print(cur_node.data, end=" -> ")
                cur_node = cur_node.next
                lenl += 1
            print("\nLength of linked list:")
            print(lenl)

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
    
    def del_node(self, key):
        
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data !=key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def choose(self, m):
        print("\n", "Linked List Operations".center(40,"_"))
        print("\n1. Add/append a node")
        print("\n2. Prepend a node")
        print("\n3. Insert between a node")
        print("\n4. Delete a node")
        n = input("\nChoose your option")

        if n == '1':

            data = input("Enter node to be added: ")
            m.append(data)
            m.printll()
            n = None
            m.choose(m)
            
        if n == '2':
            data = input("Enter node to be prepend: ")
            m.prepend(data)
            m.printll()
            n = None
            m.choose(m)
        
        if n == '3':
            node = input("Enter the node after which you want to add a new node: ")
            data = input("Enter new node: ")
            m.insert_betwn(node,data)
            m.printll()
            n = None
            m.choose(m)

        if n == '4':
            data = input("Enter node to be deleted: ")
            m.del_node(data)
            m.printll()
            n = None
            m.choose(m)

        else:
            print("\n","Wrong Choice".center(60,'*'))
            n = None
            m.choose(m)
        




llist = LinkedList()

llist.choose(llist)




'''
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("E")
#node = input("Enter the node after which you want to add a new node: ")
#data = input("Enter new node: ")
#llist.insert_betwn(node,data)
llist.del_node("C")
llist.printll()
print("\n")'''