# Hash Table
# a hash table is a data structure that provides a mapping from keys to values
# using a technique called hashing

# a python dictionary
phone_numbers = {
    'Aakash': '9489484949',
    'Hemanth': '9595949494',
    'Siddhant': '9231325312'
}
phone_numbers
phone_numbers['Aakash']
# store new phone numbers or update existing ones
phone_numbers['Vishal'] = '8787878787'
phone_numbers['Aakash'] = '7878787878'
phone_numbers
for name in phone_numbers:
    print('Name:',name, ', Phone Number:', phone_numbers[name])
# dictionaries in python are implemented using a data structure called
# hash table
# a hash table uses a list/array to store the key-value pairs
# and using a hashing function to determine the index for 
# storing or retriving the data associated with a given key
# 
# Implement a HashTable class which supports:
# Insert: insert a new key-value pair
# Find: find the value associated with a key
# Updated: update the value associated with a key
# List: list all the keys stored in the hash table
class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass 
    def find(self, key):
        """Find the value associated with a key"""
        pass
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    def list_all(self):
        """List all the keys"""
        pass

# step 1: Data List
MAX_HASH_TABLE_SIZE = 4096
data_list = [None] * 4096
len(data_list)
for item in data_list:
    assert item == None # if condition is false, will return error

# step 2: Hashing Function
# a hashing function is used to convert strings 
# and other non-numeric data types into numbers
# which can then be used as list indices
# a simple algorithm for hashing:
# 1.Iterate over the string, character by character
# 2.Convert each character to a number using python's build-in ord function
# 3.Add the numbers for each character to obtain the hash for entire string
# 4.Take the reminder of the result with the size of the data list
def get_index(data_list, a_string):
    # variable to store the result (update after each iteration)
    result = 0
    
    for a_character in a_string:
        # convert the character to a number (using ord)
        a_number = ord(a_character)
        # update result by adding the number
        result += a_number

    # Take the reminder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

get_index(data_list, 'Aakash')

data_list2 = [None] * 48

get_index(data_list2, 'Aakash')

# Insert
# insert a key-value pair into a hash table 
key, value = 'Aakash', '7878787878'
idx = get_index(data_list, key)
idx
data_list[idx] = (key, value)
# same operation
data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')

# Find
idx = get_index(data_list, 'Aakash')
idx
key, value = data_list[idx]
value

# List
pairs = [kv[0] for kv in data_list if kv is not None]
pairs


# Basic Hash Table Implementation
class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # 1.Create a list of size 'max_size' with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1.Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        # 2.Store the key_value pair at the right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1.Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        # 2.Retrieve the data stored at the index
        kv = self.data_list[idx]
        # 3.Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        # 1.Find the index for the key using get_index
        idx = get_index(self.data_list,key)
        # 2.Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]

basic_table = BasicHashTable(max_size=1024)
len(basic_table.data_list)
# insert
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')
# find
basic_table.find('Hemanth')
# update
basic_table.update('Aakash', '7777777777')
# check the updated value
basic_table.find('Aakash')


# Handling Collisions with Linear Probing
# multiple keys may have same hash
# eg. "listen" and "silent"
# this is referred to as collision
# data stored against one key may override the data stored against another
basic_table.insert('listen','99')
basic_table.insert('silent', '200')
basic_table.find('listen') #200
# to handle collisions we'll use linear probing
# 1.while inserting a key-value pair if the target index for a key 
# is occupied by another key, then we try the next index
# followed by the next and so on till we the closet empty location
# 2.while finding a key-value pair, we apply the same strategy, but instead of
# searching for an empty location, we look for a location which contains a
# key-value pair with matching key
# 3.while updating key-value pair, we apply the same strategy, but instead of 
# searching for an empty location, we look for a location which contains a 
# key-value pair with matching key
def get_valid_index(data_list, key):
    # start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # get the key value pair stored at idx
        kv = data_list[idx]

        # if it is None, return the index
        if kv is None:
            return idx

        # if the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx

        # move to the next index
        idx += 1

        # go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0 

data_list2 = [None] * MAX_HASH_TABLE_SIZE
get_valid_index(data_list2, 'listen') # 655
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
get_valid_index(data_list2, 'silent') # 656


# Hash Table with Linear Probing
class ProbingHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        # 1.Create a list of size 'max_size' with all values 
        self.data_list = [None] * max_size
    def insert(self, key, value):
        # 1.Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2.Store the key_value pair at the right index
        self.data_list[idx] = (key, value)
    def find(self, key):
        # 1.Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2.Retrieve the data stored at the index
        kv = self.data_list[idx]
        # 3.Return the value if found, else return None
        return None if kv is None else kv[1]
    def update(self, key, value):
        # 1.Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        # 2.Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)
    def list_all(self):
        # Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]

# Create a new hash table
probing_table = ProbingHashTable()
# Insert a value
probing_table.insert('listen', 99)
# Checking the value
probing_table.find('listen') #99
# Insert a colliding key
probing_table.insert('silent', 200)
# Check the old and new keys 
probing_table.find('listen') #99
probing_table.find('silent') #200
# Update a key
probing_table.update('listen', 101)
# Check the value
probing_table.find('listen')

probing_table.list_all()



# Python Dictionaries using Hash Tables
MAX_HASH_TABLE_SIZE = 4096
class HashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    
    def get_valid_index(self, key):
        # use python build-in hash function and implement linear probing
        idx = hash(key) % len(self.data_list)
        return idx
    
    def __getitem__(self, key):
        # implement the logic for "find" here
        idx = self.get_valid_index(key)
        return self.data_list[idx]

    def __setitem__(self, key, value):
        # implement the logic for "insert/update" here
        idx = self.get_valid_index(key)
        self.data_list[idx] = (key, value)

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len(x for x in self)

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{}:{}".format(repr(kv[0]), repr(kv[1])),' ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs) + "\n}")
    
    def __str__(self):
        return repr(self)

# create hash table
table = HashTable()
# insert some key-value pairs
table['a'] = 1
table['b'] = 34
# retrieve the inserted values
table
# update a value
table['a'] = 99
# check
table['a']

# get a list of key-value pairs
list(table)

len(table)