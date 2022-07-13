# pylint: disable=consider-using-f-string
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# QUESTION 1: As a senior backend engineer at Jovian, you are tasked with
# developing a fast in-memory data structure to manage profile information
# (username, name and email) for 100 million users. It should allow the
# following operations to be performed efficiently:

#    Insert the profile information for a new user.
#    Find the profile information of a user, given their username
#    Update the profile information of a user, given their username
#    List all the users of the platform, sorted by username

# You can assume that usernames are unique.

# 1. State the problem clearly. Identify the input & output formats.
# Need to create a data structure which can store 100 million records, and
# perform crud operations
# The key inputs are user profiles, which contain username name and email


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(
            self.username, self.name, self.email
        )

    def __str__(self):
        return self.__repr__()


# 2. Come up with some example inputs & outputs.
edu = User("edu", "edu", "edu@example.com")
test = User("test", "test", "test@example.com")
user10 = User("user10", "user 10", "user@example.com")

users = [edu, test, user10]

# Exercise: List some scenarios for testing the class methods insert,
# find, update and list_all.

# Insert:
#  Inserting into an empty database of users
#  Trying to insert a user with a username that already exists
#  Inserting a user with a username that does not exist

#  Find:
#  check if the user exist

#  Update:
#  check if the user exist
#

#  List:
#

# 3. Come up with a correct solution. State it in plain English.
# Insert: Loop through the list and add the new user at a position that
# keeps the list sorted.
# Find: Loop through the list and find the user object with the username
# matching the query.
# Update: Loop through the list, find the user object matching the query
# and update the details
# List: Return the list of user objects.

# 4. Implement the solution and test it using example inputs.


class UserDatabaseLinear:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


database = UserDatabaseLinear()
database.insert(edu)
database.insert(user10)
database.insert(test)

user = database.find("edu")
database.update(User(username="edu", name="edu_name", email="edu_email@example.com"))
# print(user)
# print(database.list_all())

# 5. Analyze the algorithm's complexity and identify inefficiencies
# The operations insert, find, update involves iterating over a list of users,
# in the worst case, they may take up to N iterations to return a result,
# where N is the total number of users. list_all however, simply returns
# the existing internal list of users.

# Thus, the time complexities of the various operations are:

#  Insert: O(N)
#  Find: O(N)
#  Update: O(N)
#  List: O(1)

# 6 - Apply the right technique to overcome the inefficiency


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree_tuple: tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree2 = parse_tuple(tree_tuple)
# print(tree2.left.left.key)


def display_keys(node, space="\t", level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + "∅")
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


display_keys(tree2, "   ")


# QUESTION 3: Write a function to perform the inorder traversal of a binary tree.

# QUESTION 4: Write a function to perform the preorder traversal of a binary tree.

# QUESTION 5: Write a function to perform the postorder traversal of a binary tree.


def traverse_in_order(node):
    """Implementation of in order traversal of a binary tree"""
    if node is None:
        return []
    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)


def traverse_post_order(node):
    if node is None:
        return []
    return traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key]


print(traverse_in_order(tree2))
print(traverse_pre_order(tree2))
print(traverse_post_order(tree2))


# QUESTION 6: Write a function to calculate the height/depth of a binary tree

# QUESTION 7: Write a function to count the number of nodes in a binary tree


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


print(tree_height(tree2))
print(tree_size(tree2))


class TreeNodeFull:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNodeFull.height(self.left), TreeNodeFull.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNodeFull.size(self.left) + TreeNodeFull.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (
            TreeNodeFull.traverse_in_order(self.left)
            + [self.key]
            + TreeNodeFull.traverse_in_order(self.right)
        )

    def display_keys(self, space="\t", level=0):
        # If the node is empty
        if self is None:
            print(space * level + "∅")
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return (
            TreeNodeFull.to_tuple(self.left),
            self.key,
            TreeNodeFull.to_tuple(self.right),
        )

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNodeFull.parse_tuple(data[0])
            node.right = TreeNodeFull.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


# Binary Search Tree (BST)

# A binary search tree or BST is a binary tree that satisfies the
# following conditions:

# 1.The left subtree of any node only contains nodes with keys less than the
# node's key.
# 2. The right subtree of any node only contains nodes with keys
# greater than the node's key.

# It follows from the above conditions that every subtree of a binary search
# tree must also be a binary search tree.

# QUESTION 8: Write a function to check if a binary tree is a binary search
# tree (BST).

# QUESTION 9: Write a function to find the maximum key in a binary tree.

# QUESTION 10: Write a function to find the minimum key in a binary tree.

# pylint: disable=missing-function-docstring


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (
        is_bst_l
        and is_bst_r
        and (max_l is None or node.key > max_l)
        and (min_r is None or node.key < min_r)
    )

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key


tree1 = TreeNodeFull.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(is_bst(tree1))

tree2 = TreeNodeFull.parse_tuple(
    (("aakash", "biraj", "hemanth"), "jadhesh", ("siddhant", "sonaksh", "vishal"))
)
print(is_bst(tree2))


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# QUESTION 11: Write a function to insert a new node into a BST.


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


bsdtree = insert(None, edu.username, edu)
insert(bsdtree, test.username, test)
insert(bsdtree, user10.username, user10)

display_keys(bsdtree)
print(tree_height(bsdtree))


# QUESTION 11: Find the value associated with a given key in a BST.


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


bsdnode = find(bsdtree, "edu")
print(bsdnode.key, bsdnode.value)

# QUESTION 12: Write a function to update the value associated with a given
# key within a BST


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


update(
    bsdtree, "test", User("testUpdate", "test update name", "testUpdate@example.com")
)
# node = find(bsdtree, 'test')
# print(node.value)

# QUESTION 13: Write a function to retrieve all the key-values pairs stored in
# a BST in the sorted order of keys.


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


print(list_all(bsdtree))


# Balanced Binary Trees

# QUESTION 14: Write a function to determine if a binary tree is balanced.


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


print("Is balanced?", is_balanced(bsdtree))

# Balanced Binary Search Trees
# QUESTION 15: Write a function to create a balanced BST from a sorted
# list/array of key-value pairs.


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.right = make_balanced_bst(data, mid + 1, hi, root)

    return root


data = [(user.username, user) for user in users]
tree_new = make_balanced_bst(data)
display_keys(tree_new)
print("Is balanced?", is_balanced(tree_new))

# Balancing an Unbalanced BST
# QUESTION 16: Write a function to balance an unbalanced binary search tree.


def balance_bst(node):
    return make_balanced_bst(list_all(node))


# A Python-Friendly Treemap]

# We are now ready to return to our original problem statement.


class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)
