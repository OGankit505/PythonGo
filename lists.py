# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# Modifying elements
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [1, 10, 4, 5, 6]

# Slicing
print(my_list[1:4])  # Output: [10, 4, 5]

# Length of the list
print(len(my_list))  # Output: 5

# Sorting the list
my_list.sort()
print(my_list)  # Output: [1, 4, 5, 6, 10]

# Reversing the list
my_list.reverse()
print(my_list)  # Output: [10, 6, 5, 4, 1]

# Inserting elements at a specific index
my_list.insert(2, 3)
print(my_list)  # Output: [10, 6, 3, 5, 4, 1]

# Counting the occurrences of an element
count = my_list.count(5)
print(count)  # Output: 1

# Clearing the list
my_list.clear()
print(my_list)  # Output: []

# Copying the list
new_list = my_list.copy()
print(new_list)  # Output: []

# Extending the list with another list
my_list.extend([7, 8, 9])
print(my_list)  # Output: [7, 8, 9]

# Checking if an element exists in the list
if 7 in my_list:
    print("7 exists in the list")
else:
    print("7 does not exist in the list")