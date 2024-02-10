# Initializing an empty dictionary
my_dict = {}

# Using setdefault to add a new key-value pair
my_dict.setdefault('key1', []).append('value1')
print(my_dict)  # Output: {'key1': ['value1']}

# Using setdefault with an existing key
my_dict.setdefault('key1', []).append('value2')
print(my_dict)  # Output: {'key1': ['value1', 'value2']}
