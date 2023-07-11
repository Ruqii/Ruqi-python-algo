# Problem

# 1.insert the profile information for a new user
# 2.find the profile information of a user, given their username
# 3.update the profile information of a user, given their username
# 4.list all the users of the platform, sorted by username

# we need to create a data structure which can store 100 million records 
# and perfom insertion, search, update and list operations effectively

# Input
# user profiles: username, name, email
# a python class represents the information for a user
class User:
    pass
# instantiate an object of the class by calling it like a function
user1 = User()
# we can verify that the object is of the class User
user1
type(user1)
# add a constructor method to the class to store some attributes or properties
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('user created')
# create an object with some properties
user2 = User('john', 'John Doe', 'john@doe.com')
user2.username
user2.name
user2.email
# define custom methods inside a class
class User():
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}. Contact me at {}.".format(guest_name,self.name,self.email))
user3 = User('jane', 'John Doe', 'jane@doe.com')
user3.introduce_yourself('David')
# define helper methods to display user objects nicely
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self) -> str:
        return "User(username='{}', name='{}', email='{}')".format(self.username,
        self.name,
        self.email)
    def __str__(self):
        return self.__repr__()
user4 = User('jane','Jane Doe','jane@doe.com')
user4
# function __repr__ and __str__ ???

# express our desired data structure as a python class UserDatabase with four methods
class UserDatabase:
    def insert(self, user):
        pass
    def find(self,username):
        pass
    def update(self,user):
        pass
    def list_all(self):
        pass

# come up with some example inputs & outputs
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

aakash.username, aakash.email, aakash.name

print(aakash)

users
users[0].username

# 1.insert
# A.inserting into an empty database of users
# B.trying to insert a user with a username that already exists
# C.inserting a user with a username that doesn't exist
# 2.find
# A.looking for an empty database with no user
# B.looking for a user with a username that doesn't exist
# 3.update
# 4.list
# A.list an empty basebase

# Solution
# 1.Insert: loop through the list and add the new user at a position that keeps the list sorted
# 2.Find: loop through the list and find the user object with the username matching the query
# 3.Update: loop through the list, find the user object matching the query and update the details
# 4.List: Return the list of user objects

# Implement the solution
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self,user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            # break stops the loop
            # when we find the index, we don't run the i+=1
            i += 1
        # list.insert(index,obj)
        self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self,user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
user

database.update(User('siddhant','siddhant U','siddhantu@example.com'))
database.list_all()

database.insert(biraj)
database.list_all()


# analyse the algorithm's complexity and identify inefficiencies
# insert O(N)
# find O(N)
# update O(N)
# list O(1)

# how long each function might take if there are 100 million users
# %%time
for i in range(10000000):
    j = i*i


# Apply the right technique to overcome the inefficiency
# we can limit the number of iterations required for common operations
# by organising our data in a binary tree

# each node in the tree can have at most 2 children (left or right)
# nodes can have 0, 1, 2 children
# nodes that do not have children are also called leaves
# the single node at the top is called the root node
# it typically where operations like search, insertion etc.

# balanced binary search trees
# 1.keys and values: 
# each node of the tree stores a key(a username) and a value (a User object)
# a binary tree where nodes have both a key and a value
# is often referred to as a map or treemap
# because it maps keys to values
# 2.binary search tree:
# the left subtree of any node only contains nodes with keys that are 
# lexicographically smaller than the node's key 
# the right subtree of any node only contains nodes with keys that 
# lexicographically larger than the node's key
# a tree that satisifies this property is called a binary search tree
# and it's easy to locate a specific key by traversing a single path
# down from the root note
# 3.balanced tree:
# the tree is balanced 
# it does not skew too heavily to one side or the other 
# the right or left subtrees of any node shouldn't differ in height
# or depth by more than 1 level

# height of a binary tree
# number of levels in a tree is its height
# each level of a tree contains twice as many nodes as the previous level
# for a tree of height k:
# level 0: 1
# level 1: 2
# level 2: 4 (2^2)
# level 3: 8 (2^3)
# ...
# level k-1: 2^(k-1)
# if the total number of nodes in the tree is N
# N = 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
# N + 1 = 1 + 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
# N + 1 = 2^1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
# N + 1 = 2^2 + 2^2 + 2^3 + ... + 2^(k-1)
# N + 1 = 2^3 + 2^3 + ... + 2^(k-1)
# ...
# N + 1 = 2^(k+1) + 2^(k+1)
# N + 1 = 2^k
# k = log(N + 1) < log(N) + 1
# thus, to store N records we require a balanced binary search tree(BST)
# of height no larger than log(N) + 1
# insert, find and update operations in a balanced BST have time 
# complexity O(log N)
# since they all involve traversing a single path down from the root 
class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# create objects representing each node of the above tree
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0
node0.key

# we can connect the nodes by setting 
node0.left = node1
node0.right = node2

tree = node0

tree.key
tree.left.key
tree.right.key

# convert a tuple with the structure into binary tree
# left_subtree, key, right_subtree
tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))
def parse_tuple(data):

    if isinstance(data,tuple) and len(data)==3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)
tree2
tree2.key
tree2.left.key
tree2.left.left.key

tree2.left.left.key, tree2.left.right, tree2.right.left.key

# exercise
# define a tree_to_tuple

# create another helper function to display all the keys 
# in a tree-like structure for easier visualisation
def display_keys(node, space='\t',level=0):
    # if node is empty
    if node is None:
        print(space*level + '∅')
        return
    
    # if the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)

((1,3,None),2,((None,3,4),5,(6,7,8)))
display_keys(tree2)

# Traversing a binary tree

# write a function to perform the inorder traversal of a binary tree
# write a function to perform the preorder traversal of a binary tree
# write a function to perform the postorder traversal of a binary tree

# inorder traversal
# 1.traverse the left subtree recursively inorder
# 2.traverse the current node
# 3.traverse the right subtree recursively inorder

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + 
            [node.key] + 
            traverse_in_order(node.right))

tree = parse_tuple(tree_tuple)
display_keys(tree)
traverse_in_order(tree)



# preorder traversal
# 1.traverse the current node
# 2.traverse the left subtree recursively preorder
# 2.traverse the right subtree recursively preorder

def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key] +
           traverse_pre_order(node.left) +
           traverse_pre_order(node.right))
display_keys(tree)
traverse_pre_order(tree)

# postorder traversal
def traverse_post_order(node):
    if node is None:
        return []
    return (traverse_post_order(node.right) +
            [node.key] +
            traverse_post_order(node.left))
traverse_post_order(tree)


# https://leetcode.com/problems/binary-tree-inorder-traversal/
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Height and Size of a binary tree
# write a function to calculate the height/depth of a binary tree
# write a function to count the number of nodes in a binary tree

# the height/depth pf a binary tree is defined as the length of the 
# longest path from its root node to a leaf
# it can be computed recursively
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left),tree_height(node.left))

tree_height(tree)

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
tree_size(tree)

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# https://leetcode.com/problems/diameter-of-binary-tree/

# compile all the functions

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))
    def display_keys(self,space='\t',level=0):
        # if the node is empty
        if self is None:
            print(space*level + '∅')
            return

        # if the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
        
        # if the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left, space, level+1)
    def to_tuple(self):
        # if the node is empty
        if self is None:
            return None
        # if the node is a leaf
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),self.key,TreeNode.to_tuple(self.right)
    def __str__(self):
        return 'BinaryTree <{}>'.format(self.to_tuple())
    def __repr__(self):
        return 'BinaryTree <{}>'.format(self.to_tuple())
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data)==3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)
tree
TreeNode.height(tree)
TreeNode.size(tree)
tree.display_keys()
tree.traverse_in_order()
tree.to_tuple()


# Binary Search Tree
# the left subtree only contains nodes with keys less than the node's key
# the right subtree only contains nodes with keys greater than node's key
# every subtree of a binary tree must also be a binary search tree

# write a function to check if a binary tree is a binary search tree(BST)
# write a functioin to find the maximum key in a binary tree
# write a function to find the minimum key in a binary tree

def remove_none(nums):
    return [x for x in nums if x is not None]
def is_bst(node):
    if node is None:
        return True, None, None

    # is_bst_* is True or False
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                  (max_l is None or node.key > max_l) and
                  (min_r is None or node.key < max_r))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key

tree_test = TreeNode.parse_tuple((1,3,None))
is_bst(tree_test)

tree_test.left.left
is_bst_l, min_l, max_l = is_bst(tree_test.left)
is_bst_r, min_r, max_r = is_bst(tree_test.right)

tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
is_bst(tree1)

tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
is_bst(tree2)

# Storing key-value pairs using BSTs
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
# level 0
tree = BSTNode(jadhesh.username, jadhesh)
tree.key, tree.value

# level 1
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)
tree.left.key, tree.left.value
tree.right.key, tree.right.key

display_keys(tree)

# write a function to insert a new node into a BST
# 1.starting from the root node, we compare the key to be inserted 
# with the current node's key
# 2.if the key is smaller, we recursively insert it in the left 
# subtree or attach it as the left child
# 3.if the key is larger, we recursively insert it in the right 
# subtree or attach it as the right child

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tree = insert(None, jadhesh.username, jadhesh)
tree.key, tree.value, tree.parent

insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)

tree.left.key, tree.left.value, tree.left.parent.key
tree.right.key, tree.right.value, tree.right.parent.key

display_keys(tree)

# Find the value associated with a given key in bst

def find(node,key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

node = find(tree, 'hemanth')

# Update a value in a BST
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

# write a function to retrive all the key-values pairs stored in a BST in the sorted order of keys
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
list_all(tree)


# write a function to determine if a binary tree is balanced
# 1.ensure the left subtree is balanced
# 2.ensure the right subtree is balanced
# 3.ensure the difference between heights of left subtree and 
# right subtree is not more than 1
def is_balanced(node):
    if node is None:
        return True,0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l,height_r)
    return balanced, height
is_balanced(tree)

# write a function to create a balanced BST from a sorted list/array of key value pairs
# we can use a recursive strategy here
# turning the middle element of the list into the root
# recursively creating left and right subtrees
def make_balanced_bst(data,lo=0,hi=None,parent=None):
    if hi is None:
        hi = len(data)-1
    if lo > hi:
        return None

    mid = (lo + hi)//2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data,lo,mid-1,root)
    root.right = make_balanced_bst(data,mid+1,hi,root)

    return root

users
data = [(user.username, user) for user in users]
data
len(data)

tree = make_balanced_bst(data)
display_keys(tree)


# Balancing an unbalanced BST
# we first perform an inorder traversal, 
# then create a balanced BST using function defined earlier
def balance_bst(node):
    return make_balanced_bst(list_all(node))

tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

display_keys(tree1)

tree2 = balance_bst(tree1)

display_keys(tree2) 

# after every insertion, we can balance the tree
# complexity of the various operations in a balanced BST
# Insert: O(log N) + O(N) = O(N)
# Find: O(log N)
# Update: O(log N)
# List all: O(N)

# what's the real improvement between O(N) and O(log N)?
import math

math.log(100000000, 2)

# The logarithm (base 2) of 100 million is around 26. 
# Thus, it takes only 26 operations to find or update a node 
# within a BST (as opposed to 100 million).


# A Python-friendly Treemap
# 1.Insert the profile information for a new user
# 2.Find the profile information of a user, given the username
# 3.Update the profile information of a user, given the username
# 4.List all the users of the platform, sorted by username
# we can create a generic class TreeMap which supports all the operations
# specified in the original problem statement in a python-friendly manner
class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
    
    def __getitem__(self,key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)

users
treemap = TreeMap()
treemap.display()

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh
treemap.display()

treemap['jadhesh']
len(treemap)

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal
treemap.display()

for key, value in treemap:
    print(key, value)

list(treemap)

treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
treemap['aakash']


# Self-Balancing Binary Trees and AVL Trees
# AVL(Adelson-Velsky Landis) Trees
# self-balancing in AVL trees is achieved by tracking the balance factor
# (difference between the height of the left subtree and the right subtree)
# for each node 
# and rotating unbalanced subtrees 
# along the path of insertion/deletion to balance them

# in a balanced BST, the balance factor of each node is either 0, 1 or -1
# when we perform a insertion, then the balance factor of certain nodes
# along the path of insertion may change to 2 or -2
# those nodes can be "rotated" one by one to bring the balance factor back
