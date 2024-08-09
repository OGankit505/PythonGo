# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Length of a tuple
print(len(my_tuple))  # Output: 5

# Counting occurrences of an element in a tuple
print(my_tuple.count(3))  # Output: 1

# Finding the index of an element in a tuple
print(my_tuple.index(4))  # Output: 3

# Converting a tuple to a list
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Converting a list to a tuple
new_tuple = tuple(my_list)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Checking if an element exists in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(2 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Finding the minimum and maximum elements in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(min(my_tuple))  # Output: 1
print(max(my_tuple))  # Output: 5

# Sorting a tuple
my_tuple = (3, 1, 4, 2, 5)
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)  # Output: (1, 2, 3, 4, 5)

# Reversing a tuple
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)  # Output: (5, 4, 3, 2, 1)