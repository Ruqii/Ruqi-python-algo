# Linked list
# a linked list is a data structure used for storing a sequence of elements
# Head -> data,next -> data,next -> data,next -> Null

# implement a linked list hich spport:
# 1.create a list with given elements
# 2.display the elements in a list
# 3.find the number of elements in a list
# 4.retrieve the element at a given position
# 5.add or remove elements

class Node():
    pass
node1 = Node()
node1
node2 = Node()
node2
# we can have multiple variables pointing to the same object
node3 = node1
node3
# give it a ability to store a value
class Node():
    def __init__(self):
        self.data = 0
node4 = Node()
node4
node4.data
# we can change the value inside the variable
node4.data = 10
node4.data
# let's create nodes with values 2,3,5
node1 = Node()
node1.data = 2

node2 = Node()
node2.data = 3

node3 = Node()
node3.data = 5

node1.data,node2.data,node3.data

# there's a easier way
class Node():
    def __init__(self,a_number):
        self.data = a_number
        self.next = None
node1 = Node(2)
node2 = Node(3)
node3 = Node(5)
node1.data,node2.data,node3.data

# define a class for linked list
class LinkedList():
    def __init__(self):
        self.head = None

list1 = LinkedList()
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)
list1.head.data, list1.head.next.data, list1.head.next.next.data

# head - data,next - data,next - data,next - null
list1.head, list1.head.next, list1.head.next.next, list1.head.next.next.next

# add a couple of arguments
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.head.data, list2.head.next.data, list2.head.next.next.data

# add a method to print the value in a list
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.show_elements()

# add more functions
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

list2.length()
list2.get_element(0)
list2.get_element(1)
list2.get_element(2)
list2.get_element(3)


# reversing a linked list
def reverse(l):
    if l.head is None:
        return

    current_node = l.head # give head to current
    prev_node = None

    while current_node is not None:
        # track the next node
        next_node = current_node.next # give next to next

        # modify the current node
        current_node.next = prev_node 

        # swap 
        prev_node = current_node
        current_node = next_node

    l.head = prev_node

list2.show_elements()
reverse(list2)
list2.show_elements()