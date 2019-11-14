class stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
#is_empty to check if the stack is empty
    def is_empty(self):
        return self.items == []
#top_el for returning the topmost element in the stack
    def top_el(self):
        if not self.is_empty():
            return self.items[-1]
#get_stack for returning all elements in the stack
    def get_stack(self):
        return self.items

s = stack()
print(s.is_empty())
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_stack())
print(s.top_el())
