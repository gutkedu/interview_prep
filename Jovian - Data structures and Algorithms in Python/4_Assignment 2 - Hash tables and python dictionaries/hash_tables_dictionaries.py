# In this assignment, you will implement Python dictionaries from scratch
# using hash tables.

# In this assignment, you will recreate Python dictionaries from scratch using
# data structure called hash table. Dictionaries in Python are used to store
# key-value pairs. Keys are used to store and retrieve values. For example,
# here's a dictionary for storing and retrieving phone numbers using people's
# names.

phone_numbers = {
    "Aakash": "9489484949",
    "Hemanth": "9595949494",
    "Siddhant": "9231325312",
}


# Your objective in this assignment is to implement a HashTable class which
# supports the following operations:

#   Insert: Insert a new key-value pair
#   Find: Find the value associated with a key
#   Update: Update the value associated with a key
#   List: List all the keys stored in the hash table

# QUESTION 1: Create a Python list of size MAX_HASH_TABLE_SIZE, with all the
# values set to None.

MAX_HASH_TABLE_SIZE = 4096

data_list = [None] * MAX_HASH_TABLE_SIZE
print(len(data_list) == 4096)

# Hashing Function

# A hashing function is used to convert strings and other non-numeric data type
#  into numbers, which can then be used as list indices. For instance, if a
# hashing function converts the string "Aakash" into the number 4, then the
# key-value pair ('Aakash', '7878787878') will be stored at the position 4
# within the data list.

# Here's a simple algorithm for hashing, which can convert strings into numeric
# list indices.

# 1.Iterate over the string, character by character
# 2.Convert each character to a number using Python's built-in ord function.
# 3.Add the numbers for each character to obtain the hash for the entire string
# 4.Take the remainder of the result with the size of the data list


def get_index(data_list, a_string):
    # Variable to store the result updated in each iteration
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index


print(get_index(data_list, "") == 0)
print(get_index(data_list, "Aakash") == 585)

idx = get_index(data_list, "Aakash")
print(idx)

list1 = [1, 2, 3, 4, 5]
list2 = [x * x for x in list1 if x > 2]
print(list2)

# To get the list of keys, we can use a simple list comprehension
kv = ["Aakash", "34343434"]
keys = [kv[0] for kv in data_list if kv is not None]
print(keys)

# Basic Hash Table Implementation

# QUESTION 3: Complete the hash table implementation below by following the
# instructions in the comments.


class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)
# Insert some values
basic_table.insert("Aakash", "9999999999")
basic_table.insert("Hemanth", "8888888888")
# Find a value
print(basic_table.find("Hemanth") == "8888888888")
# Update a value
basic_table.update("Aakash", "7777777777")
# Check the updated value
print(basic_table.find("Aakash") == "7777777777")
# Get the list of keys
print(basic_table.list_all() == ["Aakash", "Hemanth"])

# Handling collisions with linear probing
# As you might have wondered, multiple keys can have the same hash. For instanc
# the keys "listen" and "silent" have the same hash. This is referred to as
# collision. Data stored against one key may override the data stored
# another, if they have the same hash.

basic_table.insert("listen", 99)
basic_table.insert("silent", 200)
print(basic_table.find("listen") == basic_table.find("silent"))

# To handle collisions we'll use a technique called linear probing.

# 1.While inserting a new key-value pair if the target index for a key is
# occupied by another key, then we try the next index, followed by the next
# and so on till we the closest empty location.

# 2. While finding a key-value pair, we apply the same strategy, but instead of
# searching for an empty location, we look for a location which contains a
# key-value pair with the matching key.

# 3. While updating a key-value pair, we apply the same strategy, but instead
#  of searching for an empty location, we look for a location which contains
# a key-value pair with the matching key, and update its value.

# QUESTION 4: Complete the function get_valid_index below by following the
# instructions in the comments.


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0


# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE
# New key 'listen' should return expected index
print(get_valid_index(data_list2, "listen") == 655)
# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, "listen")] = ("listen", 99)
# Colliding key 'silent' should return next index
print(get_valid_index(data_list2, "silent") == 656)

# Hash Table with Linear Probing

# We can now implement a hash table with linear probing.

# QUESTION 5: Complete the hash table (with linear probing) implementation
# below by following the instructions in the comments.


class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # Create a list of size max_size with values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2. Store the key value pair at the right index
        self.data_list[idx] = key, value

    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]

    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]


# Create a new hash table
probing_table = ProbingHashTable()
# Insert a value
probing_table.insert("listen", 99)
# Check the value
print(probing_table.find("listen") == 99)
# Insert a colliding key
probing_table.insert("silent", 200)
# Check the new and old keys
print(probing_table.find("listen") == 99 and probing_table.find("silent") == 200)
# Update a key
probing_table.insert("listen", 101)
# Check the value
print(probing_table.find("listen") == 101)
print(probing_table.list_all() == ["listen", "silent"])
