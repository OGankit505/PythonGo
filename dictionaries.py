# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # Output: John

# Modifying values
my_dict['age'] = 26
print(my_dict['age'])  # Output: 26

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

# Checking if a key exists
if 'age' in my_dict:
    print('Age exists in the dictionary')

# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, occupation

# Iterating over values
for value in my_dict.values():
    print(value)  # Output: John, 26, Engineer

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 26, occupation Engineer


    # Creating a dictionary using constructor method
    new_dict = dict(name='Alice', age=30, city='London')
    print(new_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'London'}


    # Clearing all key-value pairs in a dictionary
    my_dict.clear()
    print(my_dict)  # Output: {}

    # Copying a dictionary
    new_dict = my_dict.copy()
    print(new_dict)  # Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

    # Getting the number of key-value pairs in a dictionary
    num_pairs = len(my_dict)
    print(num_pairs)  # Output: 3

    # Getting a list of all keys in a dictionary
    keys = my_dict.keys()
    print(keys)  # Output: ['name', 'age', 'occupation']

    # Getting a list of all values in a dictionary
    values = my_dict.values()
    print(values)  # Output: ['John', 26, 'Engineer']

    # Getting the value for a specific key, or a default value if the key doesn't exist
    value = my_dict.get('name', 'Unknown')
    print(value)  # Output: John

    # Removing and returning a key-value pair from a dictionary
    pair = my_dict.pop('age')
    print(pair)  # Output: 26
    print(my_dict)  # Output: {'name': 'John', 'occupation': 'Engineer'}

    # Removing and returning an arbitrary key-value pair from a dictionary
    pair = my_dict.popitem()
    print(pair)  # Output: ('occupation', 'Engineer')
    print(my_dict)  # Output: {'name': 'John'}

    # Updating a dictionary with key-value pairs from another dictionary
    other_dict = {'age': 30, 'city': 'London'}
    my_dict.update(other_dict)
    print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'London'}
    # Creating a nested dictionary
    nested_dict = {'person1': {'name': 'John', 'age': 25}, 'person2': {'name': 'Alice', 'age': 30}}

    # Accessing values in a nested dictionary
    print(nested_dict['person1']['name'])  # Output: John

    # Modifying values in a nested dictionary
    nested_dict['person2']['age'] = 31
    print(nested_dict['person2']['age'])  # Output: 31

    # Adding a new key-value pair in a nested dictionary
    nested_dict['person1']['occupation'] = 'Engineer'
    print(nested_dict)  # Output: {'person1': {'name': 'John', 'age': 25, 'occupation': 'Engineer'}, 'person2': {'name': 'Alice', 'age': 31}}

    # Removing a key-value pair in a nested dictionary
    del nested_dict['person2']['name']
    print(nested_dict)  # Output: {'person1': {'name': 'John', 'age': 25, 'occupation': 'Engineer'}, 'person2': {'age': 31}}

    # Checking if a key exists in a nested dictionary
    if 'age' in nested_dict['person1']:
        print('Age exists in the nested dictionary')

    # Iterating over keys in a nested dictionary
    for person in nested_dict:
        print(person)  # Output: person1, person2

    # Iterating over values in a nested dictionary
    for person in nested_dict.values():
        print(person)  # Output: {'name': 'John', 'age': 25, 'occupation': 'Engineer'}, {'age': 31}

    # Iterating over key-value pairs in a nested dictionary
    for person, details in nested_dict.items():
        print(person, details)  # Output: person1 {'name': 'John', 'age': 25, 'occupation': 'Engineer'}, person2 {'age': 31}